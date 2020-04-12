# -*- mode: python -*-

import sys
sys.setrecursionlimit(5000) # or more

block_cipher = None


a = Analysis(['Z:\\src\\main\\GUI\\run_GUI.py'],
             pathex=['Z:\\src\\main', 'Z:\\src\\main\\GUI', 'Z:\\src\\main\\core'],
             binaries=[],
             datas=[('Z:\\src\\main\\core\\loading.gif', '.')],
             hiddenimports=['libsbml', 'PyQt5.sip', 'lzma', '_lzma' ,'backports.lzma'],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          [],
          exclude_binaries=True,
          name='findCP',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          console=True )
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='findCP')
