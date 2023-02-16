# -*- coding: utf-8 -*-
"""
Introductory example - Job Submit API
=====================================

This example will show how to submit a job
using the Flux Python bindings.
"""


import os
import flux
from flux.job import JobspecV1

#%%
# Here we instantiate a flux handle. This will connect to the running flux instance.
# If you were running this on a cluster with Flux, you'd likely already be able to
# connect. If you are testing out on your own, you might need to do flux start --test-size=4
handle = flux.Flux()

#%%
# This is a new jobspec, or a recipe for a flux job. You'll notice we are providing a command
# directly, along with tasks, nodes, and cores per task. You could also provide a script here.
# If we were doing this on the command line, it would be equivalent to what is generated by:
# flux mini submit --ntasks=4 --nodes=2 --cores-per-task=2 sleep 10
jobspec = JobspecV1.from_command(
    command=["sleep", "10"], num_tasks=4, num_nodes=2, cores_per_task=2
)

#%%
# This is how we set the "current working directory" (cwd) for the job
jobspec.cwd = os.getcwd()

#%%
# This is how we set the job environment
jobspec.environment = dict(os.environ)

#%%
# Let's submit the job! We will get the job id.
print(flux.job.submit(handle, jobspec))


#%%
# This could have easily been a script, e.g., ./compute.py 120
# You can continue submitting jobs to your same handle, even the same job.
print(flux.job.submit(handle, jobspec))
