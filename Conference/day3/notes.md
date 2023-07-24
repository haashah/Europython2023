## Europython day 3

21-07-2023

### Keynote

DevOps vs. AGI

DSA (Digital Services Act)


The AI regulation ACT

Sounds like a decoy. Categorises AI into banned , high risk, and no problem.

High risk = product which can change peoples life in education, welfare, loans, medical
Banned: 

Software as a service is not a product. Software not considered like a traditional product. Request documentation. there is compliance cost for the companies. Not that expensive. 
You need to ensure people they are working with AI.

Unbiased data ? There is none. ML, simple transparent algorithm. Results in stereotyped output, ML simple transparent all results in predefined fair output. 

DevOps each stage of a ML system should be auditable and replicable.
Digital systems are easily transparent. 
DSA and AIA both assume you should be auditable. 
Ordinary product law presumes capacity to prove due diligence.
Audit capacity ? Have enough people who can readd the system logs and check compliance.
GDPR enforcement is a progress. Not 

Deep Mind
Take responsibility for your product. AI responsibility don’t wait for the regulation. 
Transhumanism = 

Rights of AI ? An active discussion. Super intelligence = learning to learn that is us humans. 



Mentored sprint in Open space


What is Opensource

Definition is tricky. The source code is open. Free to use in certain scenarios

Why contribute to OSS ?

> giving back to community. If you use it then a way to give back. 
> To learn. To collaborate. 
> to build up a PoFo
> to meet new people

Things we will use today:

* Revision control. Git
* Github
* IDE

You can contribute to open source by: 
* Code
* Documentation
* Testing and reporting bugs
* Community participation ( talk, blogpost)

What is a PR ?
Pull request
Sending a message to the maintainer. Not the final product. It’s a communication. Add more code, add more tests, Can take times. A PR can hardly be done in a day or two. Only in spare time. May have a day job. 

Common workflow

github: python/cpython

Core maintainers have write access. So right workflow is making a fork to hammad/cpython. Then make changes. Push them back to your fork. Now make a PR from your fork to their repo

Pyscript
Mew (Education and teaching etc)
Physiciclearn




#### Talk : How localstack is recreating AWS with Python


On GitHub:
Localstack/localstack

A drop in replacement for AWS.

Point all your AWS tooling to AWS. Like terraform. 
docs.localstack.

How is it done ? 

AWS is huge. Use python
Reduce complexity. Fewer lines of code. 

Python SQS full implementation in 2k lines. Since it’s not a distributed system. 

Leverage open source AWS ecosystem.

Service emulators
Awslocal kinesis put-record
POST: htt//localhost:4566

Third party tools

Mhart/
kinesalite

forward_request()

Awslocal sqs create-queue

Getmoto/ moto

Service emulators.
Leverage AWS Openstource tools. Use service specifications. Defined in SMITY. They are all open source. Use Boto3. Service model, Operationmodel. 

Update ASF APIs. API methods are updated automatically using code generators. AWS has 350 services, 13000 API opes. 93 services in localstack


Services sometimes use backend services, or open the open source services. For example Redis. 
Open AWS container tools. EKS, CKS, 

Lambda:  Runtime interface emulator. 

Localstacks Web applications framework:


HTTP2 <-> ASIG Adpater -> localstack framework , Gateway-> handlerChain, 

ServiceNameParser

localstackAWS parser

Migrate to handler chain framework.

HandlerToListerAdaapter


Pluggability:

Injecting handlers to change flow of requests coming in. Starting localstack was slow. Import took 5 seconds. Localstack core (Opensrouce tools, the services,). A closed source repo localstadck ext.
Localstack / plux


Python entry points: expose code to other distributions. Setup tolls for example. Code structured as plugins. 

Third party python disbzrituions and put on pypi. Put additional functionality into localstack.
Localstack, and monkey patching.  Last years localstack talk at europython 2022

Parity:
Behaves like AWS. Supposed to dropping replacement. Engineering blog post around this. Purest. Snap shet tests. 

You can write a test we know works against AWS> you can pick and chose not fully the API operation. Get away wit 80% of it. 

OSS 
DYnamic code loading
Pick you battles. 600 API methods
Introspect
Saying team equals to calling codebrestes
Consider patterns when migrating frameworks. 

500 contirburtos.



#### Talk Cython 3.0 by Stefan Behnel

Python code which gets converted to C so you don’t have to write C

More python. In 3.0
More python. Has type annotations, python language features @dataclass @total_ordering @ufunc
Faster than ever. Better C/C++ code
More target environments
CPython 2.7 to 3.12
PyP:y, GraalVM


What was broken ?

Python >= 0.29.30 is Cython < 2

Noexcept

- C functions propagate exceptions by default!
- Extern function pointers can mismatch


What was the biggest breaking pint between python 2 and 3 ? Unicode


Who uses Cython ?

Scikit-learn scikit-image, NumPy, pandas, SciPy.org , 

Django URL dispatcher

Instagram uses Django. URLwitty model in Django.  Ran it in Python was almost 3x faster. 

Demo

Cython needs a C compiler. Which generates a binary module. 

Jupyter notebooks have python support. 

%%cython


From python.cimports.libc import math
sin_func = math.sin



def csin(x: python.double):
	return math.sin(x)

Inspect can by used on cython function. 

Average salary example. Comparing python with cython.  3 ways to calculate salary with taxes:

Numpy slicing 

@cython.ccall decorator

Do calculations in c double rather than python float object. 

@cython.ufunc
@cython.nogil
@cython

Prange instead of range. 


Lightning talks

* Faker to generate zip, docx, files. 
From faker import Faker

Faker

Works with local and remote storage. 


* Katar 

Training your muscles by repeated an exercise. Do the same exercise every time. Gives you a sense of accomplishment. Clean Code chapter 14 by Robert C Martin. 
ML/DL Kata’s. An interview question you do everyday. Neural development. Active learning is quite famous. Habit development. 21/90 days


* Wiki crawl
Yet another crawler.  github.com/julianmaurin/wikicrawl

Wikipedia -> workers -> graph database -> grafana/prometheus


* Python in our language
Have you read CPython code ?

Some fancy demo about writing if and for loops in Czech language. Adding custom operators on list for example append backwards


* ARTIS
    * Moving data around. Create matrixes. Ars = artis.Frame(‘cuda’)

	
* Fedora
    * Targets users that create code, design, Fedora 
    * Make it the the best OS for python programmers. 
    * Sudo dnf install pythyon3.12
    * Sudo def install tox installs alls versions of supported python
    * Python tox on Fedora. On GitHub actions
    * fedoralovespython.org

* f**k it 
	
* Djangogirls


Sprints tomorrow at 9:30 AM at 


Projects tmrw:

> test UI.  Work in groups
> Validate data of data frames built on top of Pedantic
	

