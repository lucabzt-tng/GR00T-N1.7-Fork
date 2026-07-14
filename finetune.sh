CUDA_VISIBLE_DEVICES=0 uv run --active python \
    gr00t/experiment/launch_finetune.py \
    --base-model-path nvidia/GR00T-N1.7-3B \
    --dataset-path /home/innovation-hacking/data/bozzetti/lerobot_data/counterstrike_benchmark_data/v9_no_audio_old \
    --embodiment-tag NEW_EMBODIMENT \
    --modality-config-path /home/innovation-hacking/bozzetti/code/TNG_Robotics_Gaming_Benchmark/models/GR00T-N1.7-Fork/data_config/counterstrike_config.py \
    --num-gpus 1 \
    --output-dir /home/innovation-hacking/data/bozzetti/models/counterstrike/gr00tn17_benchmark_FULLRELEASE \
    --max-steps 50000 \
    --global-batch-size 32 \
    --dataloader-num-workers 4
