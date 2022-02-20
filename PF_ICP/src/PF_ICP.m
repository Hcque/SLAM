% reading the plydata, 
% normalize data

NUM_PAR = 100;
NUM_ITER = 10;

par = [];

xRangeMin;
xRangeMax;




for it = 1: NUM_ITER
  % 1 motion model
  if (it == 1)
    % 0 init
    for i = 1:NUM_PAR
      par(:).w = 1 / MUM_PAR;
      
      par.tx = xRangeMin + rand()* (xRangeMax - xRangeMin);
      par.ty = yRangeMin + rand()* (yRangeMax - yRangeMin);
      par.tz = zRangeMin + rand()* (zRangeMax - zRangeMin);
      par.Rx_th = -pi + (rand()-0.5 ) * 2 * pi;
      par.Ry_th = -pi + (rand()-0.5 ) * 2 * pi;
      par.Rz_th = -pi + (rand()-0.5 ) * 2 * pi; 
##      % TODO  
##      Rt = [par.tx, ...];
##      [R0, t0] = t2T([par.tx, ...]);
##      [R,t] = ICP_Update(par(i), );
##      Rt_hat = T2t();
##      e = Rt - Rt_hat;
##      par.S = e*e';
    end

  endif
  else
    Mu = cat(1,par.x);
    Sigma = cat(S);
    gm = gmdistribution(MU, Sigma, W);
    newPar = sample(gm, NUM_PAR);
    for i = 1:NUM_PAR:
      par.x = newPar.x;
    end  
  end

  for i = 1:NUM_PAR:
    [R_p, t_p] = ICP_Update(x, pdata, pmodel);
    e_p  = f(R_p,t_p);
    par.S = e_p * e_p';
    par.tx = ...;
    
  endfor

  % 2 weight
  for i = 1:NUM_PAR
    par.w = f(tmp_points, model_points);%sum(  );
  endfor

  % 3 resample
  par = resample(par. NUM_PAR);  
end


% find the best particle
% plot the results




