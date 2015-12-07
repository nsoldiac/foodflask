from flask import Flask, render_template, request
from nltk.corpus import wordnet as wn
from nltk.corpus import words

app = Flask(__name__)

content = '''
	<h1>Some title</h1>
'''

# def english_word(word):
# 	if word in words.words():
# 		return True
# 	else:
# 		return True
# 	#return True

def gimme_synsets(word):
	synsets = wn.synsets(word)
	if synsets:
		food = wn.synset('food.n.02')
		distances = []
		for n,i in enumerate(synsets):
			dist = i.shortest_path_distance(food)
			if dist:
				synsets[n].distance = i.shortest_path_distance(food)
				distances.append(i.shortest_path_distance(food))
			else:
				synsets[n].distance = 99
				distances.append(99)

		smallest = min(distances)
		for n,i in enumerate(synsets):
			if i.distance == smallest:
				synsets[n].likely_food = True
			else: 
				synsets[n].likely_food = False

		return synsets
	else:
		return False

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return content + 'User %s' % username

@app.route('/projects/')
def projects():
	return 'The projects page'

@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return 'Post %d' % post_id

@app.route('/template/', methods=['GET', 'POST'])
def show_template():
	if request.method == 'POST':
	 	return render_template('hello.html', synsets=gimme_synsets(request.form['word'])) 
	return render_template('hello.html', synsets=gimme_synsets('onion')) 
	 

@app.route('/about')
def about():
    return 'The about page'

if __name__ == '__main__':
	app.run()


