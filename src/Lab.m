%% Fibonacci sequence

clear;
close('all');

N = 11;

n = 0 : 1 : N - 1;
F = zeros(1, N);

for i = n + 1
    F(i) = fibonacci(i - 1);
end

figure;
stem(n, F, 'LineWidth', 2);
xlabel('$n$', 'Interpreter', 'latex', 'FontSize', 14);
xlabel('$F_n$', 'Interpreter', 'latex', 'FontSize', 14);
title(['Primeros ', num2str(N), ' t\''erminos de la sucesi\''on ', ...
    'de Fibonacci'], 'Interpreter', 'latex', 'FontSize', 14);
grid('on');

%%
% @param n - The index of the n-th term of the Fibonacci sequence
%
% @return n - The value of the n-th term of the Fibonacci sequence

function F = fibonacci(n)

    if n < 2
        F = n;
    else
        F = fibonacci(n - 1) + fibonacci(n - 2);
    end

end
