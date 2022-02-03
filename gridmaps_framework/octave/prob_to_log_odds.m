function l=prob_to_log_odds(p)
% Convert proability values p to the corresponding log odds l.
% p could be a scalar or a matrix.

% TODO: compute l.
%assert(size(p) == 1);
l = log(p./(1-p));

end
