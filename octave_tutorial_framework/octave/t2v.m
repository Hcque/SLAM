
function [x] = t2v(X)
  x = zeros(3,1);
  theta = acos(X(1,1));
  theta = normalize_angle(theta);
  
  x(1,1) = X(1,3);
  x(2,1) = X(2,3);
  assert( theta <= pi && theta >= -pi, "panic theta");
   x(3,1) = theta;
end
