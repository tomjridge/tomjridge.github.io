# Parsing

I have been interested in various aspects of parsing since 2009. My
research is particularly focused on parsing general context-free
grammars, using combinator parsers. I have published several papers,
formalized various proofs about parsers in the HOL4 theorem prover,
and produced quite a few OCaml implementations to try out various
ideas.

  * **[Earley parser](https://github.com/tomjridge/tjr_simple_earley), 2016 - now**  
    My current favourite Earley parser implementation (in OCaml). A
Python version is also available from github.

  * **[P1](https://github.com/tomjridge/p1), 2015 (now inactive)**  
  A combinator parsing library for **all** context-free grammars (CFGs). The implementation is based on the verified parsing work. 

  * **[P0](https://github.com/tomjridge/p0), 2015- now**  
  A very simple combinator library, a sort-of minimal basis for combinator parsing.

  * **[Example grammars](https://github.com/tomjridge/example_grammars/), 2015 - now**  
    Used for testing parsers. See also the [blog post](/?old=2014-12-04_parsing_examples.html)

  * **Verified parsing, 2011**  
    This work produced a verified, sound and complete approach to
    combinator parsing. This introduced the idea of "good parse
    trees". The problem with this approach is that it is too inefficient
    with left-recursive grammars. See also the [blog post](/?old=2011-12-01_verified_parsing.html).
    
  * **Older parsing work** which I have now abandoned can be found
    [here](/?page=parsing_deprecated.md)




