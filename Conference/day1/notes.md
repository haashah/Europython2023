# Personal notes from talks

## Europython 2023 conference day 1 

## 19.07.2023

## Keynote:

About comminxituy, open source software, python meet-ups, participation in the community is a free gift, it’s a kindness, if you contribute to an open source project it’s out of your kindness, volunteer
Organising meet-ups, teaching a course, cintiebute code, using software, give feedback, conference talks,

Brett Cannon

Google cloud had a stall with following competition


https://colab.research.google.com/github/PicardParis/ep23/blob/main/EuroPython%202023%20Cloud%20Challenge.ipynb#scrollTo=dNqzg9ylC0G2




## Talk 1: How are we making Cpython faster

Mark Shannon


Speeding up the slowest part of the code

Where is time spent ?

Pricipaples:

> reduce redundancy
> predict future behavior
> efficient data structures


In early python 2.7 to 3.2 an object with 4 attributes took 352 bytes. 

In python 3.3 objects of same class shared the keys. But still reducndany existed

In 3.6 shrink to 192 bytes. Besides 

In 3.8 down to 160 bytes. 
But there is still a lot of redundancy.

In 3.11 down to 112 bytes since the __dict__ is gone from the object.

In 3.12 down to 96 bytes

__dict__/values 
__weakrefs__ is null

In 3.13 might be down to 80 bytes. 

From 3.2 python object size has reduced by 77%. Number of memory reads to access a value down to 80%
Java and C just need one memory read. Python in future would be same. But object size is down to 80 bytes. Compared to C++ whch is 32

Speeding up the interpreter (future goal)

The Cpython VM is a stack machine. Bytescodes operate on the stack machine.

  y = x LOAD_FAST 0 (x)
            STORE_FAST 1 (y)

The past:

3.7 sped up method calls. Avoid creating temp object on every method call.
3.8: seped up global variable access

3.11: PEP 659 specializing adaptive interpreter. 

PEP 659:

Operations are much cheaper to do as a result. Responsible for most of the speed up in 3.11. doubled the speed approximately of the interpreter. Since programs don’t spend a lot of time in interpreter not that visible. Load attribute, 
Pylon US talk on this topic can be looked at full 30 mins on this topic

In future 3.12 and onwards optimizing larger regions of code.  Partial evaluation. Evaluate whatever we can infant to not recompute it later. 

> bytecode interpretor ( partial eval)
> memory management (better object layout)
> dynamic features (specialization)
> Cycle GC
> C extension code

Python is getting faster, we expect it to keep getting faster, upgrade to most recent version. 



## Talk 2:

Making f strings faster in 3.12

Adding python 3.5

 Format your date time inside the string. Cannot have a backslash.  ‘\n.join(list)

F”string Python code “

In background its Manual parsing in C.  parser sees a fs sting  as STRING. Sends to string parser, a bunch of chars + metadata, resends it to the parser. 

So we have a tokenized mode stack

Enters f string mode. When it sees f”. When it finds a curly brace it reaches fstring_middle. It renters normal mode which starts executing python code. If it sees f” it reenters f string mode. It pops everything from the stack until it reaches the normal mode again. This allows nested f strings.
Changes in the python tokenizer: 
Call the normal tokenizer, and do post processing on its results

F”{1+1}”
How to have double quotes inside f strings? The new tokenizer allows that. Moved the old C tokenized to the new python one. 

Lib/tokenize.py

Questions: syntax highlighter for regex 


Any changes coming in the tokenizer? Its more challenging, 

How many maximum f strings can we have? PEP specifies that at least give you 5. In Cpython its at compile time






## Talk3 Hpy

 Cpython alternatives, Graph , peppy, jpytyhon, improve execution time by implementing a JIT for example, different data structures
GraalPY is 4.5 x faster than cypython


Python C API. Since Cpython is also in C it allows C extensions. It exposes a lot of internal implementation details, objects are c pointers, memory location is exposed.  PEP 620 summarizes the problems with CPython.

GraalPy is written in Java.  Java has the stator the art garbage collector. Why should a user care  ? 79x faster than. PyPy is also 25x faster. 

HPY ? A novel C API for writing python extensions. hpy.h instead of python.h 

HPy goals:

HPy is a better API for extending Python in C

> zero overhead on Cpython. Faster on alternative implementations. Better debugging, universal API, 

# include hpy.h

In the setup.py

setup_requires = [“hpy”]

Provide a universal ABI .so file to run on PyPy, Graal, RustPython. 
Compiler provides acpython library 

In benchmarks 
C API, in 3.10 is a bit slower than the HPY CPU ABI

Migrated numpy to HPy. Compared to C API. The universal ABI is a bit slower

Has a debug mode. goal is to disable unintended usage.  Leak detector is a useful feature of debug mode. 
From hpy.debug import LeakDetector
With LeakDetector() as ld:
	snippets.test_leak_stacktrace()


A demo was shown where he build numpy for 3.11  in hybrid ABI.  Then he ran it three different python versions. 3.9. 3.10, 3.11

Migrated several packages to HPY including psuitils, pillow, numpy, 

Concentration is on NumPy, to improve performance, 
Lives on GitHub.com/hpyproject/hpy

Is a cpython extension. The design of hpy API is here. The implementation of cpython extensions is in a different place. 


### Talk 4: The power of spec testing. Functional req to unit tests

BDD development: 

End user requirements are the main concern. Example short selling:

BDD scenarios for short selling. 3 scenarios. Two failures and one success. 
Trade booking engine example. Validation and then booking a trade. 

Unitests wirrten in pytest. Parametriced to validate different scenarios. Unit tests focus on functionality rather than the user behavior.  You cannot tell the changes in the system looking at unit tests. They talk about the implemented code only. How to document the intent ?

Refactoring needs unit tests to be updated. How to do you protect from regression ? 

What about tests which :

1. Cover required behavior
2. Document user behavior
3. Don’t need changing on refactoring


Spec test example

test_trader_short_sells_with_insufficient_funds_and_fails

Spec testes exists on a higher level than unit tests. So they focus on user behavior. How do you focus on the higher scale ? 

test_trader_fails_to_borrow_as_cash_settlement……..

Describing the user behavior. Making it easy to read. Makes product team collaboration easier.  You find unknown areas which were overlooked prev. Code executing in every call for example. 

Key takeaways:
1. Focus on user behavior
2. Help integration testing
3. Act as documentation for behavior
4. Create a feedback loop


Unit > integration > system

Spec testing comes at the bottom layer, faster, easier to read. 

Questions:
Behave for behavior driven tests at integration level testing. Or cucumber for example



## Talk 5: CPython panel discussion: 
Question: Python code formatters 

Black was built on the old parser. Not working with the new one. 
A variety available. 

Cpython core developer coummincation? 

Backwards incompatibility should be announced, how 


If you have C extensions, compile it and run it as early as possible. How not break 


### Talk 6:  Dynamically generated methods


Descriptors:
A class that implements __get__ behaves like a descriptor when assigned like a class attribute.

In summary

Inspect to introspect functions
inspect.Signature
A descriptor return a function


__init__subclass__  to set required descripotors. PEP-0487


### Talk 7: BDD  by Sebastian Buczynsmi


B is for Behavior

Something with the end user. 
Scenario
Given
And
When
Then



Behavior do nots:

> Record saved
> mocking where there should be stubbing


Gherkin

Human readable, executable specification. 

Dev, Tester and PM.

Collobaration
Pairing,
Reviewing Gherkin with stakeholders


Gherkin donts:

Tester, QA separately
Business team separately

Build shared understanding:
Between st

Shared understanding 
Readable Gherkin 

DOs

> use realistic, common scenarios
> be specific

Specification

DONTS:
> Don’t get into UI
> write sciprts
> Don’t be gnereeic 


Saas for subscriptions:

User access management, plans management, subscriptions, Payments

DDD Design

Domain driven design.
Look at the problem and then make decisions about modulatiryt. Domain and subdomain divivsion. Limit the scope of a BDD spec. 

Modularized software makes BDD simple. 

To simplify a Gherkin spec we need to limit the scope. Not trying to test everything at once.

Should automation layer operation on UI or API ?

UI has more dependencies so API level should be considered first.

Example:
Abstract communication protocol with AppClient. 


Don’t mock what you don’t own. 

If you upgrade the library. It won’t be caught. 

Facade design method. To create an API over component. 




## Talk 8:  LLMs from prototype to production

SPACY

Opensource librari for NLP. 
ChaptGPT can write space code

PRODIGY

Notation tools for machine learning devs

Two kinds of tasks for NLP
1. Generative (reasoning, prlbme solving, answering, paraphrasing) human readable
2. Predictive (text classification, semantic parsing, entity recorgnion) machine readable


Problems for humans have stayed the same in last 100 years. Solution could not be imagined. Humans have not been replaced by robots but by machines. Alarm clocks and window knockers (1950s a real job)

LLMs impact equivalent to the alarm clock ?

NLP in the age of LLMs ? 


Vision *1 human input is all you need 
Vision # 2: prompting is all you need 
Vision # 3: LLM produces the training data need by the. ML system. User interacts with the ML system


Understanding NLP tasks
LLMs vs Task specific models on Text classification example

Accuracy on % samples:
SST2, AG news, with GPT3-baseline


Use LLMs to make Task specific models and get best of both worlds. 

NLP in the gage of LLMs. Structured data is needed, humans are needed, fast prototyping is also needed, need to work with models, open source is very important.

Humans versus prompting
SQL vs 


Example at
prodicy.ai/features/large-language-models

Unstructured to structured data = spacy-llm 


Being easy does not mean systems should replace current one, they should also be good. Specific is better. Use LLMs to create data needed for these models. 


Lightning talks

>

AI tournament happening.
Video game for python bots

https://github.com/europython2023gametournament/supremacy


>

Securing Opensrouce software act, GDPR, 

>

AWS lambda loves python 3.11

AWS lambda improved pefromacne from 3.10 to 3.11. runtime from 110 ms to 98 ms. 45 ms to 38 ms.

You can use your own container to run lambda from inside ECR. Even though AWS doesn’t offer 3.11 yet they are Using NIX with python and terraform and docker to run 3.11 in lambda


>

Llama 2

Llama is a research model released by Facebook could be used for all LLMs.  Training on 40% data than llama 1. Openaccess model, how can you run llama2 on your MacBook ?

Gave a live demo

> change a lambda function 


Lambda x:x



> a curious bug with list comprehensions



Spy: static python

Statically typed

Fast as C, pythonic as python

Compiled and interpreted.


*.spy instead of *.py 

Goals


SPy. Metaprogramming part of interpreter
     Rungtime part of compiler


> learning python through blocks\

