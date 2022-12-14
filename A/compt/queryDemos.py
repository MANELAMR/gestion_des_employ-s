#***(1)Returns all customers from customer table
from A.compt.views import emp


customers = emp.objects.all()

#(2)Returns first customer in table
firstCustomer = emp.objects.first()

#(3)Returns last customer in table
lastCustomer = emp.objects.last()

#(4)Returns single customer by name
customerByName = emp.objects.get(name='Peter Piper')

#***(5)Returns single customer by name
customerById = emp.objects.get(id=4)

#***(6)Returns all orders related to customer (firstCustomer variable set above)
firstCustomer.order_set.all()

#(7)***Returns orders customer name: (Query parent model values)
order = emp.objects.first() 
parentName = order.customer.name

#(8)***Returns products from products table with value of "Out Door" in category attribute
products = emp.objects.filter(category="Out Door")

#(9)***Order/Sort Objects by id
leastToGreatest = emp.objects.all().order_by('id') 
greatestToLeast = emp.objects.all().order_by('-id') 


#(10) Returns all products with tag of "Sports": (Query Many to Many Fields)
productsFiltered = emp.objects.filter(tags__name="Sports")

'''
(11)Bonus
Q: If the customer has more than 1 ball, how would you reflect it in the database?
  
A: Because there are many different products and this value changes constantly you would most 
likly not want to store the value in the database but rather just make this a function we can run
each time we load the customers profile
'''

#Returns the total count for number of time a "Ball" was ordered by the first customer
ballOrders = firstCustomer.order_set.filter(product__name="Ball").count()

#Returns total count for each product orderd
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1

#Returns: allOrders: {'Ball': 2, 'BBQ Grill': 1}


