import sublime
import sublime_plugin
import os
import glob
import subprocess

C = {}
DEFAULT_CONTENT = """//SPDX-License-Identifier: Unlicense
pragma solidity ^0.8.4;

import "hardhat/console.sol";

contract Contract {

}"""

class CreateSolidityContractCommand(sublime_plugin.WindowCommand):
  def run(self):
    hardhat_config = 'hardhat.config.ts'
    open_folders = self.window.folders()
    for path in open_folders:
      contents = os.listdir(path)
      if hardhat_config in contents:
        C['PROJECT_ROOT'] = path

      # find contracts folder.
      if 'contracts' in contents:
        C['CONTRACTS_DIR'] = os.path.join(C['PROJECT_ROOT'], 'contracts')
      else:
        print('contracts directory doesn\'t exist')
        contracts_path = os.path.join(C['PROJECT_ROOT'], 'contracts')
        os.makedirs(contracts_path)

      # create a new solidity contract.
      # new_file_at {"dirs": ["/home/zberwaldt/workspace/_bankless-dao/roots/contracts"]}
      self.window.run_command('side_bar_new_file', {
        "paths": [C['CONTRACTS_DIR']]
      })

class CreateSolidityTestCommand(sublime_plugin.WindowCommand):
  def run(self, paths=[], name=""):
    print('create solidity test...')
    view = self.window.show_input_panel(
      'NAME YO FILE:', 
      name, 
      functools.partial(self.on_done, paths, False), 
      None, 
      None
    )
    self.window.focus_view(view)

class CreateSolidityScriptCommand(sublime_plugin.WindowCommand):
  def run(self):
    print('create solidity script...')

class InitializeHardhatProjectCommand(sublime_plugin.WindowCommand):
  def run(self):
    print('initializing hardhat project...')
    folder = os.getcwd()
    print(folder)
    # subprocess.Popen(['touch', 'file.txt'])


