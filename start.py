import subprocess


def run_training():
    # 构建原始命令行命令
    command = [
        'python', 'realesrgan/train.py',
        '-opt', 'options/finetune_realesrgan_x4plus_pairdata.yml',

    ]

    # 执行命令
    subprocess.run(command, check=True)


if __name__ == '__main__':
    run_training()
