import subprocess


def run_training():
    # 构建原始命令行命令
    command = [
        'python', 'inference_realesrgan.py',
        '-n', 'RealESRGAN_x4plus',
        '-i','./data/46data/hot/test/lq',
        '--model_path','./experiments/pretrained_models/RealESRGAN_x4plus.pth'
    ]

    # 执行命令
    subprocess.run(command, check=True)


if __name__ == '__main__':
    run_training()