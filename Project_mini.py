#!/usr/bin/env python
# coding: utf-8

# # Импортируйте библиотеку pandas как pd. Загрузите датасет bookings.csv с разделителем ;. Проверьте размер таблицы, типы переменных, а затем выведите первые 7 строк, чтобы посмотреть на данные. 

# In[1]:


import pandas as pd


# In[23]:


book = pd.read_csv('Desktop/Karpov материалы/bookings.csv',sep=';')
book.head()


# In[20]:


book.shape


# In[25]:


book.head(7)


# In[27]:


book.dtypes


# # Приведите названия колонок к нижнему регистру и замените пробелы на знак нижнего подчеркивания.

# In[29]:


book.columns


# In[67]:


book = book.rename(columns={'Is Canceled' : 'Is_Canceled',
                    'Lead Time' : 'Lead_Time', 
                    'arrival full date' : 'arrival_full_date',       
                    'Arrival Date Year' : 'Arrival_Date_Year', 
                    'Arrival Date Month' : 'Arrival_Date_Month', 
                    'Arrival Date Week Number' :  'Arrival_Date_Week_Number',
                    'Arrival Date Day of Month' :  'Arrival_Date_Day_of_Month', 
                    'Stays in Weekend nights' : 'Stays_in_Weekend_nights',
                    'Stays in week nights' : 'Stays_in_week_nights', 
                    'stays total nights' : 'stays_total_nights', 
                    'Reserved Room Type' :  'Reserved_Room_Type', 
                    'Assigned room type' : 'Assigned_room_type',
                    'customer type' :  'customer_type', 
                    'Reservation Status' : 'Reservation_Status', 
                    'Reservation status_date' :   'Reservation_status_date'})


# In[68]:


book


# # Пользователи из каких стран совершили наибольшее число успешных бронирований? Укажите топ-5.

# In[84]:


book


# In[107]:


book.query('is_Canceled == 0')     .Country    .value_counts()


# # На сколько ночей в среднем бронируют отели разных типов?
# 

# In[112]:


book .groupby('Hotel',as_index=False) .aggregate({'stays_total_nights':'mean'}).round(2)


# # Иногда тип номера, полученного клиентом (assigned_room_type), отличается от изначально забронированного (reserved_room_type). Такое может произойти, например, по причине овербукинга. Сколько подобных наблюдений встретилось в датасете?

# In[116]:


book[['Assigned_room_type','Reserved_Room_Type']].head()


# In[127]:


book.query('Assigned_room_type  !=  Reserved_Room_Type')


# In[128]:


book.query('Assigned_room_type  !=  Reserved_Room_Type').shape[0]


# # Проанализируйте даты запланированного прибытия. 
# – На какой месяц чаще всего успешно оформляли бронь в 2016? Изменился ли самый популярный месяц в 2017?
# – Сгруппируйте данные по годам и проверьте, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждый из периодов.

# In[ ]:


#– На какой месяц чаще всего успешно оформляли бронь в 2016? Изменился ли самый популярный месяц в 2017?


# In[131]:


book .groupby(['Arrival_Date_Year','Arrival_Date_Month'],as_index=False) .aggregate({'Reserved_Room_Type':'count'})


# In[ ]:


#– Сгруппируйте данные по годам и проверьте, на какой месяц бронирования отеля типа City Hotel отменялись чаще всего в каждый из периодов.


# In[160]:


book.query('Hotel == "City Hotel" and is_Canceled ==1')


# In[161]:


(
    book
    .query('Hotel == "City Hotel" and is_Canceled ==1')
    .groupby('Arrival_Date_Year')
    .Arrival_Date_Month
    .value_counts()
)


# # Посмотрите на числовые характеристики трёх переменных: adults, children и babies. Какая из них имеет наибольшее среднее значение?

# In[172]:


book[['Adults','Children','Babies']].mean()


# In[173]:


book[['Adults','Children','Babies']].describe()


# # Создайте колонку total_kids, объединив children и babies. Отели какого типа в среднем пользуются большей популярностью у клиентов с детьми?

# In[177]:


book['total_kids'] = book.Babies + book.Children


# In[181]:


book['total_kids']


# In[178]:


book .groupby('Hotel',as_index=False) .aggregate({'total_kids':'mean'}).round(2)


# In[185]:


book .groupby('Hotel',as_index=False) .aggregate({'total_kids':'mean'}).round(2).max()


# # Создайте переменную has_kids, которая принимает значение True, если клиент при бронировании указал хотя бы одного ребенка (total_kids), и False – в противном случае. Посчитайте отношение количества ушедших пользователей к общему количеству клиентов, выраженное в процентах (churn rate). Укажите, среди какой группы показатель выше.

# In[187]:


book['have_kids'] = book['total_kids']>0


# In[189]:


book


# In[207]:


book.query('have_kids == False and is_Canceled == 1').shape[0]


# In[213]:


no_kids_churn = book.query('have_kids == False and is_Canceled == 1').shape[0] / book.query('have_kids == False').shape[0]
no_kids_churn = round(no_kids_churn *100,2)


# In[214]:


no_kids_churn


# In[217]:


yes_kids_churn = book.query('have_kids == True and is_Canceled == 1').shape[0] / book.query('have_kids == True').shape[0]
yes_kids_churn = round(yes_kids_churn *100,2)


# In[218]:


yes_kids_churn

