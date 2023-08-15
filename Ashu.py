from flask import Flask,render_template

FAI=Flask(__name__)

@FAI.route('/wish')
def wish():
    return 'Hai How are you'



@FAI.route('/first')
def first():
    return render_template('first.html',name='shahanaj',age=23)
if __name__=='__main__':
    FAI.run(debug=True)

