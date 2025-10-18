This directory is a miniature tutorial to machine learning, the way of the future programming for my personal career and personal projects. We will utilize TensorFlow, a lightweigt and user friendly approach to machine learning interface, which will also be the biggest player in my future big project. 

It is good to understand a couple of things: What is machine learning? How can machines learn? What are the types of way in which a machine can learn based on input and output?
All of that and more, later on in this read me.

Machine Learning
    It is a branch of artificial intelligence that allows computers to learn from data by processing said data into its developing models and algorithms program or system.

    A ML learning lifecycle, that defines the development, deployment and maintenance is composed of the following processes:
    -> problem definition: define the problem you want your ML model to solve
    -> data collection: collect the datasets that defines the way model will be trained.
    -> data cleaning and preprocessing: create the condition for which the data should be processed correctly. Take things out that affect the data being interpreted per the desired solution, standardize the way data is read and processed, ensure data is prepared for meaningful analysis.
    -> exploratory data analysis(EDA): begin testing data behavior when passing through the filters and various checkpoints. This is the process where you will see trends and patterns as data is studied.
    -> feature engineering and selection: 
    -> model selection
    -> model training
    -> model evalutation and tuning
    -> model deployment
    -> model monitoring snd maintenance


    Machine Learning Concepts:
    This is a list of all individual concepts inside of machine learning and what they are within the universal scope of any ML project or theory:
    1) Artificial Intelligence:
    -> mimics human functions for data processing and pattern recognition
    -> Not all AI is machine learning, as particular solutions can be implemented with conditional clauses without the use of pattern recognition.

    2) Algorithm: 
    -> set of rules to obtain the expected output based on a given input.
    -> a univeraal topic in computing, it is used for sorting, searching, data encrypting and data analysis.
    -> they are the directives and, ultimately, the solution to a given problem.
    -> the main purpose of the algorithm is to process data.

    3) Data:
    -> the information used to make decisions and provide ----.
    -> this is the input provided to algorithms, and is made of data types from primitive to complex, including numbers, text, images, videos, dictionaries, JSON objects, database columns, dataset rows, etc.

    4) Model:
    -> mathematical representation that's meant to recognize patterns in data and to create representations or classifications based on those patterns.

    5) Model Fitting:
    -> fine tuning the model and modifying its parameters to find the best match between the data given and the desired outcome.
    -> this is the process of training a model to accept similar data parameters in varying range to better recognize these patterns on variety.
    -> this data set exists to dictate how well a data model is genuinely learning instead of just remembering data or patterns.

    6) Data training:
    ->

    7) Data testing:
    -> a dataset utilized to dictate and evaluate how well a machine learning model works. It includes inputs and their correct answers.

    8) Features(independent variables):
    -> specific information or characteristic used to help the model make predictions.
    -> extracting features is usually significant for a model being trained successfully.

    9) feature engineering:
    the process of creating new features from existing raw data to improve a model's performance.
    -> requires the creativity to take previous features into more meaningful ones, be it by transformation(re shaping the feature) or combination(mixing multiple features) of these features.

    10) feature scaling:
    -> also known as normalization or standardization of data, it is the process of transforming numerical features into a similar scale which prevents larger ranges from dominating the model algorithmic process and thus, bias more to those and avoid other features.

    11) dimensionality:
    -> refers to the amount of features analized by the machine learning model
    -> larger dimensionality means a harder time to find patterns, so its a good rule of thumb to avoid large dimensionality set once models hae begun learning.
    -> dimensionality reduction in machine learning is often implemented to ensure feature columns are reduced but features in and of themselves are not removed from the data analysis process.

    12) target(the dependent variables)
    -> this is te output based on the input, with the input being the feature.

    13) instance:
    -> it is also called a sample, and it begins learning from these. Think of them as beginning points of reference. it is a complete unit of data that contains all features.

    14) label:
    -> is the known correct output associated with an instance in supervised learning.
    -> useful for teaching a supersives model, since they provide the correct answer for the supervised model to classify. 

    15) model complexity:
    -> it dictates the difficulty for training the model, and how sofisticated the model is for predicting patterns. More elaborate models are capable of learning from more features or parameters and recognize more difficult patterns.

    -> to better think of the model complexity, we can use the polynomial order of a regression line. A simple linear regression, for example would use only two parameters to find the point of interception and slope. More complex models, like in a quadratic sample or trace, would take about 5 parameters and find all distinct points of interceptions and slope for each individual feature per desired output. 

    16) bias:
    -> this term refers to how limited or inflexible the model's assumptions are for reading underlying patterns in the data. A higher biased model makes strong and simple assumptions, inclining the output to a more linear outcome and is overall less flexible to data being input. A lower bias can increase curves in its graphical representation, and generally means the data model is more flexible.
    Higher biased training can produce more consistent predictions over different training sets. 

    17) variance:
    -> this term refers to the flexibility a data model can have. Typically, higher flexibility can cause less generalized data interpretation and could be prone to overfitting a model if used unwise. High variance is very sensitive to small changes on output based on inputs, and can produce significantly different predictions based on variance of datasets. 


    ***NOTE -- training our model requires a proper balance(or ratio) of biases to variances, where the model is optimized at the point where the least number of total errors is discovered. The proper complexity(x axis) to the least amount of errors(y axis) where the aforementioned points where established is typically the section we want to reach, where the model has not been overfitted or underfitted.

    Overfitting usually happens when the model reads more of the noise and learns less of the true underlying patterns, like a student memorizing answers but not truly internalizing concepts, so the model behaves more like a machine and less like a human brain. This can happen when a model is too complex for the data, or its been trained for far too long.

    Underfitting happens when a machine learning model is too simple to capture the important patterns in the data, kind of the same as following the simple directives without paying much or any attention to the underlying values or patterns on the data. SO it follows through, but does not really learn on more varaint examples. This can result in poor performance in testing and data. 


    A rule of thumb to keep in mind is the following: the less complex a model is, the higher the bias and lower the variance, and vice versa. 

    18) noise:
    randowm variations or errors in data that don't represent true underlying patterns; they ty pically arise from random spikes in sensor reading or errors in data collection; ergo, avoid large errors in data collection and ignore those large fluctuations as relevant data. 

    19) validation and cross validation:
    a strategy utilized for determining the balance and fit of our model for our desired interpretation and data as input without underfitting or overfitting. 

    -> validation is the act of training the model you developed on data it has not recieved before

    -> cross validation is training the model on various subsets of that data, which would mean taking that validation criteria and cross examining with varying aspects of that criteria. 

    20) regularization:
    -> a method or discipline for keeping things under check; it adds constraints for data processing to avoid overfitting. Likewise, be careful to not regularize too much, since it can make data prone to overfitting.

    21) batch, epoch and iteration:
    -> a batch a subset of training data that is processed together in a single set of model training rather than in a single model at once. Instead of making large processes it would process various batches of processes that amount to the desired volume to train as a whole.
    -> an iteration is a single pass through a batch of data
    -> an epoch is the entire process of the various iterations for training data.
    -> models require multiple epochs to learn in an effective manner, with each epoch refining the model. Likewise, too much refining by submitting large epochs can result in overfitting.


    23) parameter:
    -> they are information that the model learns when training from the data. This is the ultimate goal from the training process. They include all the weights and biases to learn the exact output and minimize errors. 

    24) hyperparameters:
    configurations settings used to control the learning process; it is set before training begins. Hyperparameters can include: batch sizes, number of iterations, number of epochs, number of layers in a neural network. Essentially, these are the more controlled variables for training our models.

    25) cost functions(loss functions):
    -> the function that dictates how incorrect the models are based on their desired output. We train for the purpose of minimizing this loss parameter. It is done by using a math equation for finding the numerical and statistical difference between the desired output and the actual output. 

    26) gradient descent:
    -> mathematical approach that helps us find the point at which the model's error is diminishing

    27) learning rate:
    -> hyperparameter that determines how much a model can adjust its parameters in response to errors during training. Makes adjustments in how it learns its data

    28) evalutation:
    -> this indicates in numerical fashion how well the model learns on data it has not seen before. Depending on the model, some of these models will utilize specific metrics to evaluate. 

    Three ML categories exist:
        1. Supervised Learning - trains models on labeled data to predict or classify new unseen data. This model makes prediction and compares them to the ouput, adjusting itself to reduce errors and improve accuracy over time. The goal is to make accurate predictions on new unseen data. 

        This ml method can be applied to two different kinds of problems:
            a. Classification: where the output is a categorical variable. Studies a scenario to predict whether an action or an outcome will be performed or not. Or whether it is true or not.

            b. Regression: Where the output is a continuous variable. Studies data to potentially predict value or project something in a specific way.
        
        This is the step by step followed by SUpervised learning:
            1. Collect labeled data: collects data where each input to be processed is a known output.

            2. Split the data set: division of data into training data and testing it.

            3. Train the model: feed the training data to a suitable supervised learning algorithm.

            4. validate and test the model. evaluate the model using testing data that is unknown to the model

            5. depploy and predict on new data.

        2. Unsupervised learning - finds patterns or groups in unlabeled data, like clustering or dimensionality reduction.

        3. Reinforcement Learning - learns though trial and error to maximize rewards, ideal fro decision making tasks.
    Additional types of ML categories:
        1. self supervised learning: it is often considered as a subset of unsupervised learning, where it generates its own labels from the data recieved without any manual labeling. Currently, it has become its own field, such as LLMs.

        2. semi supervised learning - this approach combines a small amount of labeled data along with large amounts of unlabeled data. 
    

    

Tensor Flow

Pose Estimation for ML