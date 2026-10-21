#!/usr/bin/env python3
"""Deterministic checks of the manuscript formulas; not a universal proof.

Independent implementation of the displayed equations. Complements, but does not replace, the repository test suite. Writes JSON only.
"""
from __future__ import annotations
import json, math, platform
from pathlib import Path
import numpy as np
import scipy
from scipy.linalg import expm
from scipy.special import xlogy

ROOT = Path(__file__).resolve().parents[1]
LN2 = math.log(2)
rng = np.random.default_rng(20261021)
X = np.array([[0, 1], [1, 0]], complex)
Y = np.array([[0, -1j], [1j, 0]], complex)
Z = np.diag([1., -1.]).astype(complex)
I = np.eye(2, dtype=complex)
P = [np.diag([1., 0.]).astype(complex), np.diag([0., 1.]).astype(complex)]
checks: dict[str, int] = {}
worst: dict[str, float] = {}

def check(name: str, residual: float, tol: float = 2e-10) -> None:
    if not np.isfinite(residual) or residual > tol:
        raise AssertionError(f'{name}: residual {residual} > {tol}')
    checks[name] = checks.get(name, 0) + 1
    worst[name] = max(worst.get(name, -np.inf), float(residual))

def unitary(n: int) -> np.ndarray:
    q, r = np.linalg.qr(rng.normal(size=(n,n)) + 1j*rng.normal(size=(n,n)))
    diag = np.diag(r)
    return q @ np.diag(diag / np.abs(diag))

def state(n: int, rank: int | None = None) -> np.ndarray:
    k = n if rank is None else rank
    a = rng.normal(size=(n,k)) + 1j*rng.normal(size=(n,k))
    m = a @ a.conj().T
    return m / np.trace(m)

def entropy(a: np.ndarray) -> float:
    w = np.linalg.eigvalsh((a + a.conj().T)/2).clip(0, 1)
    return float(-np.sum(xlogy(w, w)) / LN2)

def h2(p: float) -> float:
    if not 0 <= p <= 1: raise ValueError(p)
    return float(-(xlogy(p,p) + xlogy(1-p,1-p))/LN2)

def j2(b: float) -> float:
    if not 0 <= b <= 1: raise ValueError(b)
    if b == 1: return 1.
    # Avoid subtracting nearly equal entropies at small b.
    return ((1+b)*math.log1p(b)+(1-b)*math.log1p(-b))/(2*LN2)

def f(d: float) -> float:
    return math.sqrt(max(0, d*(1-3*d/4)))+d/2

def g(eta: float) -> float:
    return min(1., eta+(1+eta)*h2(eta/(1+eta)))

def lower(s: float, eps: float) -> float:
    c = math.sqrt(1-s*s)
    if not (0 < s < 1 and 0 < eps < c/2): raise ValueError((s,eps))
    d = s*s/(2*(1+c))+eps
    b0 = max(0., s-2*eps-2*d)/(2*math.sqrt(d))
    return max(0., j2(b0)-g(f(d))-h2(eps))

def trace_distance(a: np.ndarray, b: np.ndarray) -> float:
    return float(np.linalg.svd(a-b, compute_uv=False).sum()/2)

def partial(a: np.ndarray, da: int, db: int) -> tuple[np.ndarray,np.ndarray]:
    t = a.reshape(da,db,da,db)
    return np.trace(t,axis1=1,axis2=3), np.trace(t,axis1=0,axis2=2)

def holevo(a: np.ndarray,b: np.ndarray) -> float:
    return entropy((a+b)/2)-(entropy(a)+entropy(b))/2

def spectral(a: np.ndarray,b: np.ndarray) -> tuple[float,float]:
    p,u=np.linalg.eigh(a); q,v=np.linalg.eigh(b)
    p=p.clip(0); q=q.clip(0)
    w=np.abs(u.conj().T@v)**2
    den=p[:,None]+q[None,:]
    delta=p[:,None]-q[None,:]
    terms=np.divide(delta**2,den,out=np.zeros_like(den),where=den>1e-15)
    tri=float(np.sum(terms*w)/2)
    pc=p[:,None]*w; qc=q[None,:]*w; mc=(pc+qc)/2
    js=float(np.sum(xlogy(pc,np.divide(pc,mc,out=np.ones_like(mc),where=mc>0)) +
                    xlogy(qc,np.divide(qc,mc,out=np.ones_like(mc),where=mc>0)))/(2*LN2))
    return tri,js

# Noncommuting and rank-deficient information comparisons.
for n in [2,3,4,6,8]:
    for k in range(32):
        a=state(n,1+k%n); b=state(n,1+(k+1)%n)
        tri,js=spectral(a,b)
        check('spectral_range',max(-tri,tri-1))
        check('quantum_to_classical_information',js-holevo(a,b))
        check('sharp_scalar_information',j2(math.sqrt(min(1.,tri)))-js)

# Direct CS parametrizations, including singular endpoints.
for n in [2,3,5,8]:
    for k in range(28):
        v0,v1,r0,r1=[unitary(n) for _ in range(4)]
        sn=rng.uniform(size=n)
        if k%3==0: sn[0]=0
        if k%3==1: sn[-1]=1
        K=r1@np.diag(sn)@r0.conj().T
        c0=r0@np.diag(np.sqrt(1-sn**2))@r0.conj().T
        c1=r1@np.diag(np.sqrt(1-sn**2))@r1.conj().T
        U=np.block([[v0@c0,-v0@K.conj().T],[v1@K,v1@c1]])
        check('CS_unitarity',np.linalg.norm(U.conj().T@U-np.eye(2*n)))
        omega=state(n,1+k%n)
        tau=[v0@omega@v0.conj().T,v1@omega@v1.conj().T]
        T=v1@K@v0.conj().T
        ell=np.trace((tau[0]-tau[1])@T.conj().T)
        outs=[U@np.kron(P[x],omega)@U.conj().T for x in range(2)]
        marg=[partial(o,2,n) for o in outs]
        sig=[a for a,b in marg]; env=[b for a,b in marg]
        ds=[float(np.real(sig[0][1,1])),float(np.real(sig[1][0,0]))]
        zsum=sig[0][0,1]+sig[1][0,1]
        tri,_=spectral(*tau)
        check('coherence_replacement',abs(ell-zsum)-sum(ds))
        check('weighted_Cauchy_Schwarz',abs(ell)**2-2*sum(ds)*tri)
        for x in range(2): check('physical_environment_distance',trace_distance(tau[x],env[x])-f(ds[x]))
        eta=sum(trace_distance(tau[x],env[x]) for x in range(2))/2
        check('binary_label_continuity',abs(holevo(*tau)-holevo(*env))-g(min(1.,eta)))
        deltaH=entropy((env[0]+env[1])/2)-entropy(omega)
        check('environment_nonnegative_entropy',-deltaH)
        check('environment_branch_entropy',holevo(*env)-(entropy(sig[0])+entropy(sig[1]))/2-deltaH)

# Gibbs/workspace heat ledger with possibly rank-deficient workspace.
for k in range(60):
    a=state(2,1+k%2)
    energies=np.array([0.,.5,1.7])
    gp=np.exp(-energies); gp/=gp.sum(); bath=np.diag(gp)
    U=unitary(12)
    initial=np.kron(I/2,np.kron(a,bath)); final=U@initial@U.conj().T
    _,env=partial(final,2,6); afinal,bfinal=partial(env,2,3)
    q=float(np.real(np.trace(np.diag(energies)@(bfinal-bath)))/LN2)
    dA=entropy(afinal)-entropy(a); dE=entropy(env)-entropy(a)-entropy(bath)
    mi=entropy(afinal)+entropy(bfinal)-entropy(env)
    rel=-entropy(bfinal)-float(np.real(np.trace(bfinal@np.diag(np.log2(gp)))))
    check('complete_Gibbs_workspace_identity',abs(q+dA-dE-mi-rel))

CNOT=np.array([[1,0,0,0],[0,1,0,0],[0,0,0,1],[0,0,1,0]],complex)

def collision(s:float,eps:float) -> dict:
    c=math.sqrt(1-s*s); d=s*s/(2*(1+c))+eps
    b=s/(2*math.sqrt(d*(1-d)))
    theta=math.asin(math.sqrt(d)); gap=2*math.atanh(b)
    bath=np.diag([(1+b)/2,(1-b)/2])
    U=CNOT@expm(1j*theta*np.kron(X,Y))
    check('collision_unitarity',np.linalg.norm(U.conj().T@U-np.eye(4)))
    sig=[]; env=[]; errs=[]
    for x in range(2):
        joint=U@np.kron(P[x],bath)@U.conj().T
        a,e=partial(joint,2,2); sig.append(a); env.append(e)
        target=(I-s*X+(-1)**x*c*Z)/2
        predicted=(I-s*X+(-1)**x*(c-2*eps)*Z)/2
        check('collision_output_matrix',np.linalg.norm(a-predicted))
        err=trace_distance(a,target); errs.append(err)
        check('collision_error',abs(err-eps))
    bavg=(env[0]+env[1])/2
    q=float(np.real(np.trace(np.diag([0.,gap])@(bavg-bath)))/LN2)
    check('bare_heat_formula',abs(q-b*math.atanh(b)/LN2))
    check('finite_lower_vs_construction',lower(s,eps)-q)
    return {'bias':b,'gap_over_kBT':gap,'heat':q,'branch_errors':errs,'sigmas':sig,'bath':bath,'U':U}

for s in [0.01,.05,.1,.3,.7,.9]:
    for factor in [.0001,.01,.1,.3]: collision(s,factor*math.sqrt(1-s*s))
relaxed=collision(.05,.0025)
strict=lower(.05,.0001)
check('reference_strict',abs(strict-.4980441797133478),1e-11)
check('reference_relaxed',abs(relaxed['heat']-.31148464627710154),1e-11)
allowance=h2(.0001)+.0001*math.log2(15)
check('reference_workspace_allowance',abs(allowance-.0018637225878890273),1e-12)

for b in [.01,.2,.4478860695837214,.8,.99,.9999]:
    for m in [1,2,8,64,2048]:
        q=float(b*np.arctanh(np.arange(1,m+1)*b/m).sum()/(m*LN2))
        check('recovery_lower',j2(b)-q)
        check('recovery_residual_upper',q-j2(b)-b*math.atanh(b)/(m*LN2))

# Reference-sensitive distance after input dephasing, for random reference states.
delta=[relaxed['sigmas'][x]-(I-.05*X+(-1)**x*math.sqrt(1-.05**2)*Z)/2 for x in range(2)]
e=max(np.linalg.svd(a,compute_uv=False).sum()/2 for a in delta)
for nref in [2,3,5]:
    for _ in range(24):
        rho=state(2*nref); blocks=rho.reshape(2,nref,2,nref)
        diff=sum(np.kron(delta[x],blocks[x,:,x,:]) for x in range(2))
        check('reference_sensitive_distance',np.linalg.svd(diff,compute_uv=False).sum()/2-e)
# Basis input saturates the bound, not merely a random lower estimate.
check('basis_attains_channel_bound',abs(max(np.linalg.svd(a,compute_uv=False).sum()/2 for a in delta)-e))

report={'status':'passed','seed':20261021,'checks':checks,'max_residuals':worst,
 'total_checks':sum(checks.values()),'finite_values':{'strict_lower_bound':strict,
 'relaxed_heat':relaxed['heat'],'relaxed_errors':relaxed['branch_errors'],
 'relaxed_bias':relaxed['bias'],'relaxed_gap_over_kBT':relaxed['gap_over_kBT'],
 'workspace_allowance':allowance,'strict_with_allowance':strict-allowance},
 'crossover':{str(r):j2(1/math.sqrt(1+4*r)) for r in [0,.01,.1,1,10,100]},
 'environment':{'python':platform.python_version(),'numpy':np.__version__,'scipy':scipy.__version__},
 'scope':'Finite formula/matrix checks of this manuscript implementation. Not the source repository test suite, an arbitrary-dimension proof, or an experiment.'}
(ROOT/'build'/'documents').mkdir(parents=True,exist_ok=True)
(ROOT/'build'/'documents'/'manuscript_numerics.json').write_text(json.dumps(report,indent=2)+'\n')
print(json.dumps({k:report[k] for k in ['status','total_checks','finite_values','environment']},indent=2))
