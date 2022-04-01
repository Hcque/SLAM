function [R, t] = ICP_Update(ptmp,pmodel, R0, t0, L)
  n,_ = size(ptmp);
  _ptmp = ptmp;
  
  for it = 1:L
    [kidx, D] = knnsearch(pmodel, _ptmp, 'k', 1);
    E = pmodel[kidx]-_ptmp;
    _cov = E*E';
    [U,S,Vh] = svd(_cov);
    R = Vh*U;
    if (det(R) < 0) 
      [U,S,Vh] = svd(R);
      S[end] *= -1;
      R = U*S*Vh;
    endif
    
    _ptmp = _ptmp * Rt;
    
  endfor
  [R,t] = Rt;
end