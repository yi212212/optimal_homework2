X = [2,0;0,1;0,0];
y = [3;2;2];
n = 2;
cvx_begin
    variable w(n)
    minimize( square_pos(norm( X * w - y, 2 )) )%目标函数
    subject to
        %norm(w, 1) <= 1;                        %约束条件	
        %square_pos(norm(w, 2)) <= 10;           %约束条件		
cvx_end	