define(['jquery'], function($){
    var CustomWidget = function () {
    	var self = this;
		this.WakeUpWhenUserDoSomethingWithGoods = function() {
			// TODO Add new item to order
			// TODO Remove item from order
			// TODO Update / Change quantity of items

		};
		
		this.WillCalculateGoodsSum = function() {
			// TODO Take prices from goods
			// TODO Calculate sum from goods' prices
			// TODO check if goods sum ok
			// TODO Tell user "Success. Sum is calculate"

		};

		this.WillChangeLeadBudget = function() {
			// TODO check if goods's sum not equal null
			// TODO change sum
			// TODO check if budget change sum from goods?
		};





		this.callbacks = {
			render: function(){
                                // ... здесь описываются действия для отображения виджета...
				console.log('render');
				return true;
			},
			init: function(){
                                // ... используется для передачи инфы стороннему серверу...
				console.log('init');
				return true;
			},
			bind_actions: function(){
                                // ... события предпринимаемые пользователем. пример: клик...
				console.log('bind_actions');
				return true;
			},
			settings: function(){
				return true;
			},
			onSave: function(){
				alert('click');
				return true;
			},
			destroy: function(){
                                // ... нужен когда при выключении нужно удалить элементы виджета...
				
			},
			contacts: {     // TODO remove as useless 
					//select contacts in list and clicked on widget name
					selected: function(){
						console.log('contacts');
					}
				},
			leads: {        // TODO is that "selected:" needs me for work? 
					// select leads in list and clicked on widget name
					selected: function(){
						console.log('leads');
					}
				},
			tasks: {        // TODO remove as useless
					//select taks in list and clicked on widget name
					selected: function(){
						console.log('tasks');
					}
				}
		};
		return this;
    };

return CustomWidget;
});
