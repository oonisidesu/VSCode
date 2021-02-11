import subprocess

# macのアプリケーションフォルダ内のアプリケーションをコマンド（python）で起動する
# open -a 「アプリケーション名」
subprocess.run('open -a マルハン', shell=True)