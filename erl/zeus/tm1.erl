%% author Liferenko[]

-module(tm1).
-export([sample/1, fact/1, tail_fact/1, sample_tuple/1, is_palindrom/1, simple_sort/1, simple_sort_lower/1, bubble_sort/1, bubble_sort_lower/1, test/0, start_test/0]).


sample(X) -> X * X.

% without tail recursion
fact(0) -> 1;
fact(N) -> N * fact(N-1).

% with tail recursion
tail_fact(N) -> tail_fact(N, 1).

tail_fact(0, Res) -> Res;
tail_fact(N, Res) -> tail_fact(N-1, Res * N).


% workin' with tuples and atoms
sample_tuple(X) ->
    case X of
        {1, true} -> false;
        {2, false} -> true;
        {_, _} -> wow
    end.


% palindrom
is_palindrom(List) 
    when ((tl(List) == []) 
    or (List == [])) -> true;
is_palindrom([_H | T]) ->
    Last = lists:last(T),
    if _H == Last -> is_palindrom(lists:sublist(T, length(T) - 1));
        true -> false
    end. 


%% Types of sorts
simple_sort(List) -> simple_sort(List, []).

simple_sort([], Result) -> Result;
simple_sort([_H | T], Result) ->
   if
        T == [] -> simple_sort(T, [_H | Result]);
        _H > hd(T) -> simple_sort(lists:append([hd(T) | Result], [_H | tl(T)]));
     true -> simple_sort(T, [_H | Result])
    end.

%% Bubble sort
bubble_sort(List) -> bubble_sort(List, [], 0).
bubble_sort([], Result, N) ->
    if
        N == length(Result) - 1 -> Result;
        true -> bubble_sort(lists:reverse(Result), [], N+1)
    end;

bubble_sort([_H | T], Result, N) ->
    if
        T == [] -> bubble_sort(T, [_H | Result], N);
        _H > hd(T) -> bubble_sort([_H | tl(T)], [hd(T) | Result], N);
        true -> bubble_sort(T, [_H | Result], N)
    end.


%% Lambda-functions


simple_sort_lower(List) -> 
    Func = fun(X, Y) -> 
            if X > Y -> true; 
                true -> false 
            end 
        end,

    simple_sort(Func, List, []).

simple_sort(_Func, [], Result) -> Result;
simple_sort(_Func, [_H | []], Result) ->    simple_sort(_Func, [], [_H | Result]);
simple_sort(_Func, [_H | T], Result) ->
    Buf = _Func(_H, hd(T)),
    if
        Buf == true -> simple_sort_lower(lists:append([hd(T) | Result], [_H | tl(T)]));
     true -> simple_sort(_Func, T, [_H | Result])
    end.




bubble_sort_lower(List) ->
    Func = fun(X,Y) -> if X > Y -> true; true -> false end end, 
    bubble_sort(Func, List, [], 0).


bubble_sort(_Func, [], Result, N) ->
    if
        N == length(Result) - 1 -> Result;
        true -> bubble_sort(_Func, lists:reverse(Result), [], N+1)
    end;

bubble_sort(_Func, [_H | []], Result, N) -> bubble_sort(_Func, [], [_H | Result], N);

bubble_sort(_Func, [_H | T], Result, N) ->
    Buf = _Func (_H, hd(T)),
    if
        Buf == true -> bubble_sort(_Func, [_H | tl(T)], [hd(T) | Result], N);
        true -> bubble_sort(_Func, T, [_H | Result], N)
    end.





%% Real task
start_test() ->
    spawn(tm1, test, []).

test() ->
    receive
        _ -> 
            io:format("запустилось! Выполняю... ~n"),
            exit(crash)
    end.
