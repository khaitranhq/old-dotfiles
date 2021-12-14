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
}, {
    'dir':
    'ultorex/automation_selenium',
    'git':
    'git@gitlab.com:ultorex/testing-group/automation_selenium.git'
}, {
    'dir': 'ultorex/ultorex-be/ticker',
    'git': 'git@gitlab.com:ultorex/backend-group/ticker.git'
}, {
    'dir': 'linux-control-center',
    'git': 'git@github.com:lioaslan/linux-control-center.git'
}, {
    'dir':
    'ultorex/ultorex-infra/infra-building',
    'git':
    'git@gitlab.com:ultorex/infra-group/infra-building.git',
}, {
    'dir': 'competitive-programming',
    'git': 'git@github.com:lioaslan/competitive-programming.git'
}, {
    'dir': 'email-signatures',
    'git': 'git@github.com:lioaslan/email-signatures.git'
}, {
    'dir':
    'ultorex/ultorex-be/hibtc-web-back',
    'git':
    'git@gitlab.com:ultorex/backend-group/hibtc-web-back.git'
}, {
    'dir': 'ultorex/ultorex-be/mine',
    'git': 'git@gitlab.com:ultorex/backend-group/mine.git'
}, {
    'dir': 'ultorex/ultorex-be/news',
    'git': 'git@gitlab.com:ultorex/backend-group/news.git'
}, {
    'dir': 'ultorex/ultorex-be/order-bot',
    'git': 'git@gitlab.com:ultorex/backend-group/order-bot.git'
}, {
    'dir': 'ultorex/ultorex-be/xex-back',
    'git': 'git@gitlab.com:ultorex/backend-group/xex-back.git'
}, {
    'dir': 'todo',
    'git': 'git@github.com:lioaslan/ToDo.git'
}, {
    'dir': 'ultorex/ultorex-be/trade-bot',
    'git': 'git@gitlab.com:ultorex/backend-group/trade-bot.git'
}, {
    'dir': 'koindex/koindex-fe/web',
    'git': 'git@gitlab.com:koindex/clients-group/koindex-web.git'
}, {
    'dir':
    'ultorex/ultorex-fe/ultorex-nextjs-web',
    'git':
    'git@gitlab.com:ultorex/clients-group/ultorex-nextjs-web.git'
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
