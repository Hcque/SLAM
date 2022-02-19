% resample the set of particles.
% A particle has a probability proportional to its weight to get
% selected. A good option for such a resampling method is the so-called low
% variance sampling, Probabilistic Robotics pg. 109
function newParticles = resample(particles)

numParticles = length(particles);

w = [particles.weight];

% normalize the weight
w = w / sum(w);

% consider number of effective particles, to decide whether to resample or not
useNeff = false;
%useNeff = true;
if useNeff
  neff = 1. / sum(w.^2);
  neff
  if neff > 0.5*numParticles
    newParticles = particles;
    for i = 1:numParticles
      newParticles(i).weight = w(i);
    end
    return;
  end
end

newParticles = struct;

% TODO: implement the low variance re-sampling
J = numParticles;
r = rand() * 1/J;
% the cumulative sum
% initialize the step and the current position on the roulette wheel
c = w(1); i = 1;
for j = 1:numParticles
  U = r + (j-1)/J;
  while (U > c) 
    i += 1;
    c += w(i);
  endwhile
  % ADD
  newParticles(i).weight = particles(i).weight;
  newParticles(i).pose = particles(i).pose;
  newParticles(i).history = cell();  
end
% walk along the wheel to select the particles
##for i = 1:numParticles
##  particles(i).weight = 1. / numParticles;
##  particles(i).pose = zeros(3,1);
##  particles(i).history = cell();
##end

end
