    print(len(to_dataframe))
    print('to drop_duplicates')
    

    #event_properties
    datos_lista_user_properties=[]
    user_id_user_properties=[]
    client_event_time_properties=[]
    uuid_user_properties=[]
    event_time_user_properties=[]
    amplitude_id_properties=[]
    for b in range(0,len(to_dataframe)):
        #print(b)

        #print(step1)
        intext_to=to_dataframe[b]['event_properties'].index
        for a in range(0,intext_to[-1]):
            #print(a)
            datos_lista_user_properties.append(to_dataframe[b]['event_properties'][a])
            user_id_user_properties.append(to_dataframe[b]['user_id'][a])
            amplitude_id_properties.append(to_dataframe[b]['amplitude_id'][a])
            uuid_user_properties.append(to_dataframe[b]['uuid'][a])
            client_event_time_properties.append(to_dataframe[b]['client_event_time'][a])

    def Merge(dict1, dict2, dict3, dict4, dict5, dict6):
        res = {**dict1, **dict2, **dict3, **dict4, **dict5, **dict6}
        return res
      
    event_properties_step2=[]
    for a in range(0,len(datos_lista_user_properties)):

        datos_lista_user=datos_lista_user_properties[a]
        user_id={'user_id2':user_id_user_properties[a]}
        amplitude_id={'amplitude_id':amplitude_id_properties[a]}
        uuid={'uuid':uuid_user_properties[a]}
        client_event_time={'client_event_time':client_event_time_properties[a]}
        numero_fila={'numero_fila':[a]}
        event_properties_step1=Merge(datos_lista_user,user_id,amplitude_id,uuid,client_event_time,numero_fila)
        event_properties_step2.append(event_properties_step1)
 
