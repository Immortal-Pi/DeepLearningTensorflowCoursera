	• Main concepts 
		○ Introduction
			§ Deep neural network
			§ Callback function
			§ CNN
				□ Convolutional 2D layer
				□ Maxpooling
				□ Image generator 
				□ Prediction from downloaded images 
		○ CNN
			§ Data cleaning methods 
			§ Image augmentation (data augmentation)
			§ Transfer learning
			§ Dropout
		○ CNN multi class models
			§ Categorical 



		○ NLP (natural language processing) - preferably use google colab?
			§ Tokenizer
			§ OOV - out of vocabulary ()
			§ Text to sequence
			§ Padding
			§ Text embeddings
			§ Vector plotting
			§ Optimization
				□ Vocab_size
				□ Max_length
				□ Embedding_dim
			§ Splitting words to subtokens - Subword Tokenization
			§ GRU and LSTM (theory)
			§ We can use CNN layers and dropout layers 
			§ Sequence models
		○ NLP prediction
			§ Create a list of sentences
			§ Tokenizer.fit_on_text
			§ Word_index
			§ Preprocessing the dataset
				□ Convert text to sequence
				□ Iterate over the each sentence sequence 
				□ Ngram - create a list of split by appended 1 at the end 
				□ Padding
				□ Each xs- length -1 y - last index
				□ Convert y to categorical (one hot encoding)
				□ 
			§ Create model and predict
			§ Generating new text
				□ Seed sentence 
				□ Tokenize the input text
				□ Pad the sequence
				□ Predict
				□ Add to seed sentence
			
	
	
	
	
	• Time series (tf.data.Dataset.from_tensor_slices())
		○ Trend 
		○ Seasonality
		○ Noise 
		○ Auto correlation 
		○ Moving average
		○ Smoothing window
			§ Dataset
			§ Window
			§ Flat_map
			§ Map
			§ Shuffle
			§ Batch
		○ Choosing learning rate in optimizer
			§ Learning rate scheduler
		○ RNN and LCMs - on sequence data
		○ Implement Lambda layers
		○ Using LSTM
		○ Forecating results 
		
		○ Plot_series
		○ CNN and LSTM
		○ Model forecast
		○ Call back for val_mae
		○ Decayed_learning_rate
			
