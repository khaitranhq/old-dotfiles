#!/usr/bin/python3

import os

WORKSPACE_DIR = '/home/leo/Workspace/'

LIST_PROJECTS = [{
    'dir': 'ultorex/ultorex-infra/apps-deploy',
    'git': 'git@gitlab.com:ultorex/infra-group/apps-deploy.git'
}, {
    'dir': 'credentials',
    'git': 'git@github.com:lioaslan/credentials.git'
}, {
    'dir': 'ticket',
    'git': 'git@github.com:lioaslan/ticket.git'
}, {
    'dir': 'ultorex/ultorex-be/common',
    'git': 'git@gitlab.com:ultorex/backend-group/common.git'
}, {
    'dir': 'ultorex/ultorex-be/account',
    'git': 'git@gitlab.com:ultorex/backend-group/account.git'
}, {
    'dir': 'ultorex/ultorex-be/bb',
    'git': 'git@gitlab.com:ultorex/backend-group/bb.git'
}, {
    'dir': 'pbl6',
    'git': 'git@github.com:Linhnef/PBL6.git'
}, {
    'dir': 'ultorex/ultorex-infra/cicd-ansible',
    'git': 'git@gitlab.com:ultorex/infra-group/cicd-ansible.git'
}, {
    'dir': 'ultorex/ultorex-be/hibtc-web',
    'git': 'git@gitlab.com:ultorex/backend-group/hibtc-web.git'
}]

for project in LIST_PROJECTS:
    project_full_dir = WORKSPACE_DIR + project['dir']
    if not os.path.exists(project_full_dir):
        os.system('mkdir -p %s' % (project_full_dir))
        os.system('cd %s && git clone %s %s' %
                  (project_full_dir, project['git'], project_full_dir))
        os.system('cd %s' % (WORKSPACE_DIR))
    else:
        print('%s existed' % project['dir'])
