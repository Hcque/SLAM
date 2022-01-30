
function [X] = v2t(x)
  theta = x[3];
  X = eye(3);
  X(1,1) = cos(theta);
  X(1,2) = -1*sin(theta);
  X(2,1) = sin(theta);
  X(2,2) = cos(theta);
    
  X(1,3) = x[1];
  X(2,3) = x[2];

end
