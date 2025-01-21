# Setup environment
pip install -r requirements.txt
pip install torch==1.11.0+cu113 -f https://download.pytorch.org/whl/torch_stable.html
conda install -c conda-forge faiss-gpu

# Training
## Phase 1: Relevance-Based DocID initialization (M0)
batch_size = 4 => train tốn 7.8G
batch_size = 16 => train tốn 

bash full_scripts/full_train_t5seq_encoder_0.sh
bash full_scripts/full_train_t5seq_encoder_1.sh
bash full_scripts/full_evaluate_t5seq_aq_encoder.sh   (task=all_aq_pipline)

## Phase 2: Seq2Seq Pretraining + Initial Fine-tuning (M1)