
import attributes_class


counter = 0
x_axis1 = []
y_axis1 = []
name1 = ''
x_axis2 = []
y_axis2 = []
name2 = ''


def compare(x_axis, y_axis, name):

    if(counter==0):
        globals()['x_axis1'] = x_axis
        globals()['y_axis1'] = y_axis
        globals()['name1'] = name
        globals()['counter'] += 1
    elif(counter==1):
        globals()['x_axis2'] = x_axis
        globals()['y_axis2'] = y_axis
        globals()['name2'] = name
        globals()['counter'] += 1
    if(counter==2):

        object = attributes_class.attributes()
        object.plot_graph_compare(x_axis1, y_axis1, name1, x_axis2, y_axis2, name2)
        globals()['counter'] = 0
        clear_att()
        #x_ahmed=[2,4,6,8]
        #y_ahmed=[1,2,3,4]


        #name_a = 'ahmed'

        #object.plot_graph_compare(x_ahmed, y_ahmed, name_a, x_axis1,y_axis1, name1)



def clear_att():
    x_axis1.clear()
    y_axis1.clear()
    x_axis2.clear()
    y_axis2.clear()
    name1 = ''
    name2 = ''

