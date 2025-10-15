Chapter 0 — How to use this guide

Read chapters in order. Each chapter builds on the previous.

Keep a REPL, Jupyter notebook, or small project folder open — practicing as you read cements concepts.

When you’re ready to code, I’ll provide runnable TensorFlow examples wired to MediaPipe outputs.

Chapter 1 — What is Machine Learning? (Intuition + formal)

Intuition: ML is about building systems that learn patterns from data to make predictions or decisions without being explicitly programmed for each rule.

Formal view (supervised): Given dataset 
𝐷
=
{
(
𝑥
𝑖
,
𝑦
𝑖
)
}
𝑖
=
1
𝑁
D={(x
i
	​

,y
i
	​

)}
i=1
N
	​

 sampled from unknown distribution 
𝑃
(
𝑋
,
𝑌
)
P(X,Y), choose model 
𝑓
𝜃
f
θ
	​

 (parameterized by 
𝜃
θ) to minimize expected loss:

𝜃
∗
=
arg
⁡
min
⁡
𝜃
𝐸
(
𝑋
,
𝑌
)
∼
𝑃
[
𝐿
(
𝑓
𝜃
(
𝑋
)
,
𝑌
)
]
θ
∗
=arg
θ
min
	​

E
(X,Y)∼P
	​

[L(f
θ
	​

(X),Y)]

In practice we minimize empirical loss (training loss) over finite samples using optimization algorithms (SGD, Adam, etc).

Types of learning

Supervised (labels provided): classification, regression.

Unsupervised (no labels): clustering, dimensionality reduction, representation learning.

Self-supervised: labels constructed from data itself (predict next frame, contrastive tasks).

Reinforcement learning: learning via reward signals (not primary for pose/form correction).

Chapter 2 — Data: the center of ML

Key truth: Better data > more complex model 9 times out of 10.

Important concepts

Features vs labels: Features 
𝑋
X are inputs (pose landmarks), labels 
𝑌
Y are ground truth (e.g., “good form”/“bad form”, angle error, rep count).

Distribution — train/test should reflect real usage.

Bias/variance tradeoff — low bias (complex models) can overfit; low variance (simpler models) may underfit.

Imbalance — many “good form” vs few “bad form” examples requires balancing or class weighting.

Quality over quantity — correct labels and realistic variability (lighting, clothing, body sizes) matter most.

Practical data collection for pose apps

Record diverse people, camera angles, clothing, lighting, device types.

Record variations of correct and incorrect form intentionally (common mistakes).

Label format options:

Scalar error (continuous): angle deviation, joint distance to target.

Categorical: {good, knees_in, back_arched, elbow_flare}.

Multi-label: multiple simultaneous faults.

Temporal labels for sequences (per-frame or per-repetition label).

Data augmentation ideas (pose-specific)

Add Gaussian noise to landmark coordinates (simulate jitter).

Randomly drop or occlude joints (simulate occlusions).

Scale/shift coordinates (simulate camera zoom/translation).

Temporal augmentations: time-warping, speed variations, slicing sequences.

Chapter 3 — Feature engineering for pose data

MediaPipe gives you normalized landmarks 
(
𝑥
,
𝑦
,
𝑧
,
𝑣
𝑖
𝑠
𝑖
𝑏
𝑖
𝑙
𝑖
𝑡
𝑦
)
(x,y,z,visibility) per joint. Raw landmarks are fine but smart features improve learning.

Common feature types

Normalized pixel coordinates: Convert landmark.x * width, landmark.y * height. Or keep normalized.

Relative coordinates: Shift origin to a body reference (e.g., pelvis/hip) to get translation invariance.

Example: 
𝑥
𝑖
′
=
𝑥
𝑖
−
𝑥
ℎ
𝑖
𝑝
x
i
′
	​

=x
i
	​

−x
hip
	​

.

Scale normalization: Divide by torso length or distance between shoulders to normalize for person size.

Angles: Joint angles are extremely useful (scale- and translation-invariant).

Use vectors between joints: angle at joint B formed by A-B-C:

𝜃
=
atan2
⁡
(
∥
(
𝐴
−
𝐵
)
×
(
𝐶
−
𝐵
)
∥
,
(
𝐴
−
𝐵
)
⋅
(
𝐶
−
𝐵
)
)
θ=atan2(∥(A−B)×(C−B)∥,(A−B)⋅(C−B))

Velocities & accelerations: first/second differences across frames to capture motion dynamics.

Pairwise distances: distances between important anchors (hand to hip, wrist to shoulder).

Temporal windows: stack features across time (sliding window) for sequence models.

Visibility masks: include landmark.visibility to gate features when occluded.

Why angles?

They’re invariant to camera translation/scale (if normalized properly).

Directly meaningful for form rules (e.g., “knee angle must be > 90°”).

Chapter 4 — Model families & when to use them

I’ll pair each model with when it’s a good fit for pose/form tasks.

4.1 Linear models (Logistic regression, linear regression)

Use when: Problem is near-linear, small data, baseline, or explainability matters.

Pros: Fast, interpretable.

Cons: Limited capacity.

4.2 Decision trees / Random Forest / Gradient Boosted Trees (XGBoost, LightGBM)

Use when: Tabular engineered features (angles, distances), less need for temporal modeling.

Pros: Work well with moderate data, robust to feature scales, interpretable feature importance.

Cons: Require engineered features; less natural for sequence data.

4.3 Neural Networks
4.3.1 MLP (Multilayer Perceptron)

Use when: Fixed-length vector inputs per sample (single frame or stacked window).

Pros: Flexible, simple.

Cons: Needs feature engineering for spatial/temporal structure.

4.3.2 CNNs (1D temporal conv / 2D conv on heatmaps)

Temporal 1D conv: Use when your data is a sequence of feature vectors. Good for capturing local temporal patterns.

Spatial 2D conv on heatmaps: If you render landmark heatmaps or use images, CNNs are ideal.

4.3.3 RNNs (LSTM / GRU)

Use when: Sequential modeling with long-ish temporal dependencies (rep cycles).

Pros: Good for sequences, variable length.

Cons: Training can be slower; transformers have been taking over.

4.3.4 Transformer-based / attention models

Use when: Complex temporal relationships, focus on long-term dependencies, or multi-scale attention needed.

Pros: Powerful; handle variable sequence lengths with parallelizable training.

Cons: Data-hungry; heavier compute.

4.3.5 Graph Neural Networks (GCNs) for skeletons

Use when: Explicit skeleton structure matters — joints connected by bones; great for pose recognition and action detection.

Pros: Encodes skeletal topology; state-of-the-art in many human pose tasks.

Cons: More complex to implement; needs graph-convolution libraries.

4.3.6 Temporal ConvNets (TCN)

Use when: Capture long temporal context with causal convolutions; often outperform RNNs in stability/speed.

Chapter 5 — Losses, metrics, evaluation
Loss functions

Classification: Cross-entropy (binary or categorical). Also focal loss for imbalance.

Regression: MSE (L2), MAE (L1), Huber loss (robust to outliers).

Structured outputs: Sequence-level losses, DTW-based losses, or CTC for alignment tasks.

Multi-task: Weighted sum of per-task losses; consider dynamic weighting.

Metrics

Classification: Accuracy, precision, recall, F1, ROC-AUC, PR-AUC (use PR for imbalanced).

Regression: MAE, RMSE, R².

Sequence tasks: segment-wise F1, IoU for temporally annotated segments.

Calibration metrics: ECE (expected calibration error) if you use predicted probabilities for decisions.

User-centered metrics: time-to-detect-first-error, false positive rate per session.

Evaluation protocol

Train/Val/Test split: Ensure no subject leakage (e.g., same person in train and test) to reflect real generalization.

K-fold cross-validation for small datasets.

Temporal split if distribution changes over time.

Subject-wise split: essential for human-centric models.

Chapter 6 — Optimization & training recipes
Optimizers

SGD + momentum: stable, sometimes better generalization.

Adam / AdamW: fast convergence, good default.

Ranger/Lookahead etc: advanced; use only if you know tradeoffs.

Learning rates

Use learning rate schedules: step decay, cosine annealing, cyclical LR, or warmup + decay.

Tip: LR is the most important hyperparameter — do LR range test (fast).

Regularization

Dropout, weight decay, early-stopping, data augmentation.

BatchNorm/LayerNorm for stable training.

Gradient clipping for RNN/transformer instability.

Batch size

Bigger batch = faster training per epoch but might harm generalization. Use learning rate scaling if increasing batch size.

Checkpoints & reproducibility

Save checkpoints frequently; use consistent random seeds for reproducibility (note: complete determinism is platform-dependent).

Chapter 7 — Handling sequences & temporal modeling (practical)

For a personal trainer, temporal context is essential (form is dynamic).

Pipeline approaches

Frame-wise model + smoothing/post-filter

Predict per-frame labels; then apply temporal smoothing (median filter, majority vote) to reduce flicker.

Simpler but may miss context.

Sliding-window approach

Build dataset of windows (e.g., 1–3s of landmarks), label windows, use CNN/TCN/MLP on flattened window.

Sequence-to-sequence / Bi-directional models

Use LSTM/Transformer across entire rep to generate per-frame predictions (needs entire sequence at inference; not always real-time causal).

Hybrid

Use causal model for real-time (e.g., TCN with causal convolutions) and offline transformer for detailed analysis.

Example input shapes

Per-frame MLP: input vector size = n_landmarks * features_per_landmark (e.g., 33 * 3 = 99).

Windowed sequence for LSTM: (batch, time_steps, feature_dim).

Chapter 8 — Explainability, uncertainty, interpretability

SHAP / LIME: Per-input feature attributions (works well for tabular/MLP).

Grad-CAM like methods for CNNs if using image inputs.

Calibrated probabilities: Use temperature scaling or Platt scaling.

Uncertainty estimation: MC dropout, deep ensembles, or Bayesian NN techniques to get epistemic/aleatoric uncertainty — useful to avoid giving confident but wrong advice.

Chapter 9 — Deployment & efficiency

You will likely deploy on CPU/mobile — so plan accordingly.

Steps

Export model: for TensorFlow → SavedModel → TFLite (for mobile/embedded). For PyTorch → TorchScript or ONNX.

Quantize: post-training dynamic/static quantization to int8 or float16 for speed and size reduction.

Prune: weight pruning for compression (use carefully).

Edge runtimes: TFLite, TensorFlow Lite Micro, ONNX Runtime Mobile.

Measure real-world latency & accuracy tradeoffs.

Model size/perf tips

Use smaller architectures or knowledge distillation from big teacher models.

Use fewer input features — compute angles for only target joints to reduce input dimension.

Use TFLite delegates (GPU, NNAPI) when available.

Chapter 10 — Data engineering, MLOps, and production considerations

Version data with DVC or delta tables; track labels, annotators, and dataset versions.

Continuous evaluation in production; collect failure cases and retrain iteratively.

Monitoring: track model drift, statistical shifts, latency, error rates, and false positives.

Human-in-the-loop: allow users to confirm or correct feedback to gather labeled corrections.

Chapter 11 — Ethics, bias, privacy

Get consent to record and store user videos and landmarks.

Minimize personally identifiable information (store only landmarks if possible).

Test across body types, skin tones, ages, and ability levels — avoid biased feedback that favors a limited demographic.

Provide safe, conservative suggestions rather than rigid instructions for risky moves.

Chapter 12 — Advanced ML topics worth knowing (nuances)

Representation learning & contrastive learning: learn a pose embedding space from unlabeled data (useful for few-shot problems). Example: SimCLR-style training on sequences.

Meta-learning & few-shot: useful if you want to adapt to a new user quickly with few examples.

Graph neural networks (GCN/ST-GCN): treat skeleton as graph with spatial+temporal edges — state-of-the-art for action recognition.

Multi-task learning: jointly predict rep counts, form-categories, and per-joint corrections to improve generalization.

Self-supervision: predict temporal order, masked joint prediction, or future frames — useful when labels are scarce.

Chapter 13 — Practical ML pipeline for your project (end-to-end recipe)

Concrete recipe that you can implement.

1) Data collection & labeling

Capture raw videos with MediaPipe landmarks saved per-frame as JSON/CSV.

Label: per-frame (good/bad), per-rep, or continuous error scores.

Split data subject-wise.

2) Preprocessing

For each frame/sequence:

Extract landmarks: (x,y,z,vis) for each selected landmark (33 joints).

Convert to relative coordinates w.r.t. hip center.

Normalize by torso length (distance shoulder-hip).

Compute joint angles for key joints.

Stack features for a temporal window if using sequences.

3) Model prototyping (start simple)

Baseline: RandomForest on hand-engineered angles/distances.

Stronger: LSTM/TCN over sequences of angles.

Advanced: ST-GCN over skeletal graph for sequence classification/regression.

4) Training

Use Adam (lr 1e-3) with ReduceLROnPlateau or cosine schedule.

Train until val metric plateaus; use early stopping.

Log metrics and tensorboard visualizations.

5) Evaluation

Subject-wise test split; compute F1, precision/recall; analyze failure cases.

6) Export & deploy

Convert to TFLite with quantization; integrate with MediaPipe runtime or run model separately on frames/landmarks.

7) Inference loop (real-time)

Capture frame → MediaPipe pose process() → extract landmarks → preprocess → run model → postprocess smoothing/thresholds → show visual feedback.

Chapter 14 — How MediaPipe and TensorFlow join the fray (practical integration)

This is the exact link between your sensor (camera) and ML system.

Roles

MediaPipe: feature extractor — provides reliable, real-time structural data (landmarks + visibility + segmentation).

TensorFlow: learning system — consumes landmarks / engineered features and outputs diagnosis/feedback/rep-counts.

Concrete integration flow

MediaPipe (pose)

Input: camera frames (BGR from OpenCV; convert to RGB).

Output: results.pose_landmarks (33 landmarks), pose_world_landmarks (meters), segmentation mask.

Preprocess

Choose reference point (e.g., hips).

Relative coordinates: subtract reference.

Normalize by scale (shoulder width).

Compute angles and velocities; create feature vector f_t.

TensorFlow ingestion

Use tf.data.Dataset to stream CSV/TFRecord sequences efficiently.

Batch and pad sequences if necessary.

For real-time inference, convert your model to accept single frames or sliding windows.

Model backend

tf.keras model: MLP / LSTM / TCN / small transformer.

Output: classes (softmax), probabilities, or regression error values.

Post-processing

Apply temporal smoothing (exponential moving average, majority voting).

Threshold probabilistic outputs conservatively.

Map model output to actionable feedback text and visuals.

Deployment

Convert SavedModel → TFLite (with/without quantization).

In mobile/edge: integrate TFLite runtime and run inference on preprocessed landmark tensors.