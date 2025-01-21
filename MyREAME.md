# Setup environment
pip install -r requirements.txt
pip install torch==1.11.0+cu113 -f https://download.pytorch.org/whl/torch_stable.html
conda install -c conda-forge faiss-gpu

# Training
## Phase 1: Relevance-Based DocID initialization (M0)
batch_size = 4 => train tốn 7.8G
batch_size = 16 => train tốn 10G
batch_size = 64 => train tốn 23G (mất 221:07:53)

bash full_scripts/full_train_t5seq_encoder_0.sh
bash full_scripts/full_train_t5seq_encoder_1.sh       (chỉ là lấy checkpoint của M0 rồi train tiếp)
bash full_scripts/full_evaluate_t5seq_aq_encoder.sh   (task=all_aq_pipline)

## Phase 2: Seq2Seq Pretraining + Initial Fine-tuning (M2)
bash full_scripts/full_train_t5seq_seq2seq_0_1_pipeline.sh