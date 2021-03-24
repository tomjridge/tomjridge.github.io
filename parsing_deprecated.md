# Parsing (old, deprecated)

These are projects which I have largely abandoned:

  * P3 is a combinator parsing library that can parse all CFGs, whilst
    offering $O(n^3)$ performance (which I consider optimal for
    real-world usage: there are approaches that can do better than
    $O(n^3)$, but the real-world overhead is currently unacceptable,
    and the implementation complexity is high).

  * E3 is an Earley parser which is used by P3.

  * P4 is a combinator parsing library that improves on P3 in 2 main ways:
    * The library user has tight control over the parsing, allowing
      better real-world performance than P3.
    * Various extensions are supported that allow to go beyond
      context-free grammars. For example, indentation-sensitive
      parsing is possible, based on allowing infinitely-many
      nonterminals in the grammar.

    The downside is that the interface to P4 is more complicated than that for P3.


Older links are:

- P3: New versions of P3 are now available from github at
<https://github.com/tomjridge/p3>. At the moment the documentation is
on the github wiki for P3 at <https://github.com/tomjridge/p3/wiki/P3>.

The best documentation for P3 internals is the extended version of the
following paper: Tom Ridge.  Simple, efficient, sound and complete
combinator parsing for all context-free grammars, using an oracle. In
Proceedings of SLE 2014. [ridge14sle.pdf](resources/doc/ridge14sle.pdf)
[extended version](resources/doc/ridge14sle_extended.pdf).


- E3 is available from github at
<https://github.com/tomjridge/e3>. The
[examples](https://github.com/tomjridge/e3/blob/master/src/e3_examples.ml)
should give some guidance on usage.

- P4 is available from github at <https://github.com/tomjridge/p4>,
but there is no documentation at the moment. It was a version of P3
with support for dynamically generated grammars. For example, you
could parse a grammar of the form `G_n -> <the number n> | <the number
n> G_{n+1}`:

```ocaml
(* _G 1 parses "1", or "1" followed by _G 2; in general, _G n parses
   the number n, optionally followed by _G (n+1); there are an infinite
   number of nonterminals (_G n) generated lazily on demand *)

let _G = ref (fun n -> failwith "")

let _ = _G := fun n -> 
  let an = a (string_of_int n) in
  let alts = lazy(alts[
    (rhs an) >> (fun s -> c s);
    (an >-- (!_G (n+1))) >> (fun (x,y) -> (c x)^y)])
  in
  mkntparser_lazy (mk_pre_parser ()) alts
```

- `P5_scala` is a version of P4 for Scala, available at
<https://github.com/tomjridge/p5_scala>. Currently not in a very
polished state. Mostly useful for me to try out Scala.
