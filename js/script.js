define(['jquery'], function($){
    var CustomWidget = function () {
    	var self = this;
		this.wakeUpWhenUserDoSomethingWithGoods = function() {
			// TODO Add new item to order
			// TODO Remove item from order
                        // TODO Update / Change quantity of items
                        // TODO grab order items' articles aka SKU
		};
		
		this.calculateGoodsSum = function() {
			// TODO Take prices from goods
			// TODO Calculate sum from goods' prices
			// TODO check if goods sum ok
			// TODO Tell user "Success. Sum is calculate"

		};
                this.changeOrderList = function() {
                        let orderListId = 123 // TODO find it in Drommel API docs;
                        // TODO change multilist by goods' articles (SKU)
                };
		
                this.changeLeadBudget = function() {
			// TODO check if goods's sum not equal null
			// TODO change sum
			// TODO check if budget change sum from goods?
		};


		this.sendInfoToGoogleSpreadSheet = function() {
                        // TODO send
                        // self.crm_post(
                        //      'https://TODO webhook URL',
                        //      {
                                // Send POST data
                                name: person_name['name'],
                                phones: person_name['phones'],
                                emails: person_name['emails']
                                },
                        //      function() {},
                        //      'json'
                        //);
                };


		this.callbacks = {
 			// SDK карточки - линк на php-файлы на сайт
			var sdk_url = 'http://drommel.com.ua/webhooks/widget/';
			var sdk_url_back_link = 'http://drommel.com.ua/webhooks/widget/sdk_back/link.php';      	   
			var sdk_url_back_search = 'http://drommel.com.ua/webhooks/widget/sdk_back/search.php';
                        
                        loadPreloadedData: function () {
                                return new Promise(_.bind(function (resolve, reject) {
                                        //Сделаем запрос на удаленный сервер
                                        self.crm_post(
                                        sdk_url,
                                        {
                                            id: {number},
                                            sku: {string},
                                            name: {string},
                                            price: {string},
                                        },
                                        function (msg) {
                                                //Приведем элементы к нужному формату и зарезолвим
                                                resolve(msg);
                                        },
                                        'json'
                                        );
                                }), this);
                        },
                        loadElements: function (type, id) {
                                return new Promise(_.bind(function (resolve, reject) {
                                        //Сделаем запрос на удаленный сервер
                                        self.crm_post(
                                        sdk_url,
                                        {},
                                        function (msg) {
                                                //Приведем элементы к нужному формату и зарезолвим
                                                resolve(msg);
                                        },
                                        'json'
                                        );
                                }), this);
                        },
                        linkCard: function (links) {
                                return new Promise(_.bind(function (resolve, reject) {
                                        //Сделаем запрос на удаленный сервер
                                        self.crm_post(
                                        sdk_back_url_link,
                                        links,
                                        function () {
                                           //Мы не обрабатываем ошибки, которые могли произойти на вашей стороне, в данном блоке Вы можете выполнить
Ваш код
                                        },
                                        'json'
                                        );
 
 
                                        resolve();
                                }), this);
                         },
                         searchDataInCard: function (query, type, id) {
                                return new Promise(_.bind(function (resolve, reject) {
                                        self.crm_post(
                                        sdk_back_url_search,
                                        {
                                        query: query,
                                        type: type,
                                        id: id
                                        },
                                        function (msg) {
                                                resolve(msg);
                                        },
                                        'json'
                                        );
                                }), this);
                        },

// -----------


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
