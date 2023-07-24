## Europython 2023 day 2

### 20-07-2023

#### Keynote: The future of microprocessors

Multiprocessors can only speedup parallel programs. A web browser for example will only go 4x speedup

The multicore consensus is 

More transistors are not as useful anymore as they were. Dennard+RISC (less power with smaller transistors). OOO archtiure multicore, then into Amdahl’s law and now end of easy Moore.


Power density means heat is generated. So after Pentium 4 architecture had to change it was getting too hot.

At 7nm and 125W power limit half the die has to be off. Meaning the silicon cannot be on all the time.

28nm , 20 nm, 7 nm chips AMND and Apple have 5 nm. Transisters smaller than 20nm cost more than 20 nm items so it sort of end of Moor’es law. 
Moving from planar transistors at 20 nm we got leaky transistors that don’t turn off / on so easily. So we made them vertical making FinFET. Now we could fit more transistors. 28 nm FinFET is 22 nm. 20 nm FinFet is 14 or 16 nm. 12 nm, 10 nm 8,7,6,

Economic issue:

To maintain Moore’s law we need more people to work on the research.

Intel predicted in 2010 manufacturing
65nm > 45 nm > 32 nm > 22 nm > 14 nm

All the predictions were late by few years. \

Now we have lesser companies capable of doing leading edge fabrication. Intel , Samsung, TSMC are only on leading edge. Rest are a bit behind > 10 nm fabrication. Everbody uses the same lithography. TSMC and Samsung prettyy close 52M per process. Intel was at 37M in 2017. Mid 2023 we are at 292M N3 for TSMC, Intel at 237M at 7. Samsung probably at 250M 

Lithography: printing metal. Master copy which makes copies on pieces of silicon. To get from deep UV to extreme UV 32 nm light. How to make extreme UV light ? A beam of 13 nm light comes out onto a scanner. These machines are expensive and now much bigger than before. Every generation of this machine is much bigger than before. 

The evolution

We can use more tranasiters than we do today. Supersacler OOO designs moving tiny ARMS’s big.LITTLE. Which have little cores and power burning big cores more power efficient. This design is all about power efficiency. Moving out to what we process is also changing. DSPs, GPUs, Deep learning engines now. IPUs, DNNs

8/16 bit or smaller processing can 
3 to 5 TOPS per W
Spiking Neural networks

A new performance race

From 3.94 TOPS in 2012 to 4000 today. 

M1 Max design

11 Tops Neural engine
Close to 240W desktop desktop chips

Transisters are chasing again. From FinFET to nanowire and nano sheet.  Possible maybe CFET 

Most of the research spending on now is packing and advanced packing. 

Largest chip ever made. For machine learning. By TSMC with 2.6 trillion transistors at 7nm  process. 



#### Talk 1 : Python on ARM

Clouds are also now offering ARM.
Python on AArch64. ArArch64 is the 64 extension of ARM processor introduced in 2011. CPython is written in portable C.  Enablement effort when arm instances became available in public cloud.  started in 2020. Analyzed 2920 packages in PyPI. Over 100 packages have been moved. 
Speed.python.org doesn’t have AArch64 benchmarks. 

Python 3.11 and 3.10 on Neoverse (N1)

Neovers-N2 intances on Alibaba cloud. 

Distribution channels: installed in different ways. Ppt,. Compile from source, default package. 
All packages compile with GCC are compiled agains ARMv8

Recompile Cpython against more recent CPU. With MCPU flag you can autodetect host architecture. GCC11, GCC12, GCC13 were also tried. Neoverse cpus are relevantly new

AWS benchmarks for single process. Run on a variety of flavors C7g, C6i. ( Intel xeon 3rd gen). Lost in all benhcamrsk to x86 except a few scenarios. Similar across different CPtyhon versions.

For multiprocess. Run an instance of pyperformance for every CPU present.  ARM did much better than x86 since all vcpus are actuall cores.


Python on Windows on ARM:

Python 3.11 Windows on ARM is officially supported. 

Test top 520 packages. 70% succeeded. Linaro. You can build a package for WoA using cross compilation. 

Python on WoA. Windows 11 on ARM can run x64 binaries via emulation but much slower. Non native binaries work but much slower than native arm64. 

Tensorflow Lite, for deploying on edge devices, smaller devices, 
Model optimization: Contriving 

Tensforflow packages on PyPI compatible AArch64. 

For PyTorch from version 1.8.0 available for AAarch64. 

Apache TVM, Added support for packing, CLI, 
OpenBLAS enabled SVE for Neoverse-V1
NumPY: implemented faster math routines in numpy


What gaps to do we have

Aaarch64 is in tier 2. Needs to be move to tier 1 to bring on par with x86

Aarch64/arm64, not present on the speed center

Windows on Aarm is just getting started. No PyTorch and Tensforlow packages yet

Performance on single process performance on AAarch64 is lagging behind x86.

What can we do?

Start to migrate your workloads to ARM 
Start building and testing your python package on ARM platform if you build your own package.
Engage directly with us.

ARM developer program.  www.arm.com/developerpgrogram
A discord server with ARM employees to ask questions. 



#### Talk 2:  Instrumenting CPython using eBPF

eBPF ?

Network filter pgroams. Filter to accept/reject IP packets. 
Not just for network packets. Its capabilities is beyond packet filtering. Alexei Stravaoitov and Daniel Brokmann, epbf.io

Configuring CPython

3.5 above.
With-dtrace
systemTap (provides an interface on running a 


Probes

Displaying the probes
Readelf -n ./python

fucntion__entry(filename, funcname, line) 
function__return(filename, funcname, linen)

fc__start(generation)
gc__done(long collected)
import__find__load__start(str module name)
import__find_load__done(str module name, found) audit(str event, void tuple)


Instrumentation: Tracing and Profiling. Trace and performance.  Measures 

BCC = BPF compiler collection

github.com/iovisor/bcc

eBPF program

Impor argparse
From bcc import BPF, USDT,

Bpftrace

A high level tracing language for eBPF
Created by Alastair Robertson

Py-spy
Sam;ling profiler for python programs. Reads the memory of the python program.  

A sample program was profile during py-spy. Flame graph. Create stack trace of compiled software. 

Profiler (based on eBPF)

Created a flame graph by gprofiler.  IT is System wide profiler. Profiles all python programs running on the . Pyperf is a couple up

Why is eBPF important ? 
Faster access to memory. Access to memory much faster than pyspy . No context switches. Executed in kernel space so they are faster. Event driven. It has a JIT. Compiles ebpf program to machine code. 



#### Talk 3:


From monitora.cz



Text summarization contain false information (hallucinations) temperature parameter can help with that  if the original text is too small.

Problem 1: ChatGPT not so good for languages other than English

Problem2: ChatGPT API completion time kept going up

Problem3: summary language is wrong. 

ChatGPT -3.5 , 4.0 , Claude, Bard, Bing chat comparison


LLaMa

Works better with Czech 
HuggingFace


Training your own model is easy but replacing ChatGPT is the challenge in production. Running OpenML models could be a legal challenge with the new EU legislation,



#### Talk 4: Packaging apps with briefcase

Beeware > supported by Anaconda. Fully open source

One tool called briefcase. Packaging python applications.  Not for libraries and  websites etc (Django, flash).  A briefcase application a full code, python interrparert, dependencies, install app into bundle. 

PyOxiderzer, PyInstaller, competitors
Its cross platform, 


Pip install briefcase

Briefcase new

pyproject.toml

Filled by setup wizard.

[tool.briefcase]

formal_name = 
descxription=
long_descriptojn=
cion=
sources=
test_sources=
requires = [

]

test_requires = [

]


[tool.briefcase.app.helloworld.macOS]
Requires = []

[tool.briefacase.app.hellowrold.win]



Can be generated by a widget or just make your own pyproject.toml

Breifcase dev
Does in the background the following:

Pip install -r require
Python -m 


Briefcase create > 

X§


Some issues  > no signing on linux,
> package for other linux distress using docker
> briefcase package linux —target ubunut:kinteic

Briefcase update
Reinstall code of your ap. To update requirements, resources add flags to the command


Other features


#### Talk 5: Infrasturcure as code

Optiver the company is a trading company since e1986. 

What’s required to build you on premises infra	store.  PSACE, POWER, PDUS etc, racks, network devices, set ears, cables, wan connectivity, a long list

Monitoring is a challenge. Don’t do manual configuration of hardware, 
There is also legal regulations. So a kill switch. How easy is the infra to build from scratch ? Scale up or scale down ?
What’s infrastructure as Code ? 

Manage provisioning through code instead of manual process
Machine readable definition
Reproducibility+speed - human error = cost reduction = risk reduction
Enable orchestration
Standardizations
Declarative vs. imperative

Terraform example

OSS stack:

There is no de facto like Kubernetes. Netbox/Nautobot, NAPALM, Openstack, MAAS, Rack are interesting options. 

Step 0: The standard


Their solution :

Standard, high level definition, SDK and CLI. APIs + Web . Intent 

Provisioning pipelines> reads the intent  push the firmware, os changes 


Python ecosystem is great for these kind of problems. A 


#### Talk6: Security, securing pipit

PyPI biggest warehouse of python packages

Securing repositories since they are a huge target. = signed artifacts. If you lose a key, new key and resign. If you have millions of packages, mirrors and CDNs, how do you notify users of the new key ? 
TUF and PEP 458
The update framework = TUF. Solution 
* Sign everything
* Doesn’t sign aretifcs but only metadata files. 
* Clear process for key revocation

PEP 458
* Proposes a mimium design of TUF. For Py{PI
* Rollback freeze protection
* Explicit key revocation
* No changes for the end user

TUF spec is very complex. Long term, a lot of code. Generate metadata, 

We didn’t implement TUF in PYPI
They made RSTUF = repository service for TUF under the OpenSSF, 

RSTUF was born from implementing PEP 458 

Abstract the TUF specs. 

Design is to make it 
* Easy to deploy
* Scalability and consistency
* REST API first. Easy to integrate


RSTUF comes between the puli repo and the CD server. Github action 30-40 lines send to an exiting repository. It is easy to deploy stuff. 
RSTUF management. CLI guided processes

There is an API which can be used but there is also a CLI which doesn’t require TUF  experience. 
Step by step process. Colorful summaries.  
RSTUF is 
* Artifact agnostic
* Language agnostic
* Artifact release process agnostic
* Deploy on cloud or on premise. Uses docker, ubnerentes
Main RSTUF features:

* Bootrap
* Import existing artifacts
* Add/Remove Artifacts
* Key revocations
* Key generation

PyPI with RSTUF

TUF client flow
1. Request to dwlonad release x.y.z
2. Pip downloads TUF metadata. Validates that x.y.z exists
3. Download the artifact and validate 

Future plans:

Flixiblith on key vault and storage
Custom role deleting
Improved metadtgata management
Distributed SY

RSTUF BEATA IS OUT


#### Talk 7: Whisper AI

Popen sourced by OpenAI before ChatGPT
Only input is audio not text.

Used whisper to transcribe German into English live in meetings every Friday where non German speakers were listening. Added Whisper as participant in the meeting. 


Used python threads to start record audio, trasnrive with whisper in another thread. 


Front end is polling and rendering the subtitles

Threading vs. Multiprocessing

Threads have shared memory, can communicate via a Queue. Asynchronous code. But they cannot run in parallel. Blocked by the GIL. 

Processes: multiple isolated python instances. They communicate via Queue and PIPE. This queue pickles the data.  Multi core execution. Whisper runs on GPU so not really useful for speeding it up. 

What’s next? Whisper AI can be fast depending on th GPU .  lambdalabs.com where you can rent GPUs. 



#### Talk 8: Responding to Disasters using Open-Source NLP




Earthquake in Turkey in Feb 2023 millions affected, thousands died. 

An OCR app to parse addresses.  easyOCR, paddleOCR, tesseract, . easyOCR was used I the end. 

Initial

Disaster map app = a frontend with lat long map of people needs. Who needs what and where . Parsing tweets, post owners needs, name and phone number, address. 

Using a pretrainined model, adapt it to be useful in your use case. Process called fine tuning.  

BERT Model

Biggest change in NLP. GPT, Llama come from transformer architecture. BERT is first NLP coming from transformer 
Transformers library. Has trainer API
> Intent classification

NLP inference models were used. Zero shot text classification mode.   Transformers was used. Address parsing was tried with GPT-3. 

Hugging face hub: Github of machine learning. Models could be tried straight away. Helped with inference. 

Completely open source MLOPS pipeline

Segmenting buildings in Satellite images.  

ahbap.org 

