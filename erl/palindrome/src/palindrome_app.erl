%%%-------------------------------------------------------------------
%% @doc palindrome public API
%% @end
%%%-------------------------------------------------------------------

-module(palindrome_app).

-behaviour(application).

%% Application callbacks
-export([start/2, 
        stop/1, 
        is_palindrome_test/2, 
        target_palindrome/1, 
        reverse_list/1]).

%%====================================================================
%% API
%%====================================================================

start(_StartType, _StartArgs) ->
    palindrome_sup:start_link().

%%--------------------------------------------------------------------
stop(_State) ->
    ok.

is_palindrome_test( [], [] ) ->
    true;
is_palindrome_test( [H|T1], [H|T2] ) ->
    is_palindrome_test( T1, T2 );
is_palindrome_test( _, _ ) ->
    false.

target_palindrome( List1, List2 ) ->
    is_palindrome_test( List1, reverse_list(List2) ).
target_palindrome( List ) -> 
    target_palindrome( List, List ).


%%====================================================================
%% Internal functions
%%====================================================================

reverse_list( List ) ->
    reverse_list( List, [] ).
reverse_list( [], List ) ->
    List;
reverse_list( [H|T], List ) ->
    reverse_list( T, [H|List] ).
