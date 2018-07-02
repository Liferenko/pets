-module(palindrome_SUITE).
-include_lib("common_test/include/ct.hrl").
-export([suite/0, all/0, 
     init_per_suite/1, end_per_suite/1,
     init_per_testcase/2, end_per_testcase/2]).

%% Test cases
-export([string/1, integer/1]).


suite() -> 
    [{timetrap,{minutes,1}}].  
all() ->
    [string. integer].


init_per_suite(Config) -> 
    end.

end_per_suite(Config) ->    
    end.

init_per_testcase(Case, Config) ->
    end.
end_per_testcase(_Case, Config) ->
    end.
