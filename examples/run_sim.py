'''
Simple script for running the Covid-19 agent-based model
'''

import sciris as sc

print('Importing...')
sc.tic()
import covasim as cv
sc.toc()

do_plot = 1
do_save = 0
do_show = 1
verbose = 1
seed    = 4
interv  = 0

version  = 'v0'
date     = '2020mar31'
folder   = 'results'
basename = f'{folder}/covasim_run_{date}_{version}'
fig_path = f'{basename}.png'

print('Making sim...')
sc.tic()
sim = cv.Sim()
sim.set_seed(seed) # Set seed (can also be done via sim['seed'] = seed)
sim['n'] = 50 # Population size
sim['n_infected'] = 1
sim['n_days'] = 100 # Number of days to simulate
sim['prog_by_age'] = False # Use age-specific mortality etc.
sim['usepopdata'] = False # Use realistic population structure (requires synthpops)
sim['rel_symp_prob'] = 500.0
sim['rel_severe_prob'] = 500.0
sim['rel_crit_prob'] = 500.0
sim['rel_death_prob'] = 500.0
if interv:
    sim['interventions'] = cv.change_beta(days=45, changes=0.5) # Optionally add an intervention

print('Running...')
sim.run(verbose=verbose)

if do_plot:
    print('Plotting...')
    fig = sim.plot(do_save=do_save, do_show=do_show, fig_path=fig_path)










