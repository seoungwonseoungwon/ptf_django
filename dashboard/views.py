from django.shortcuts import render
# from .read import mapo_name
# Create your views here.
from .models import Opexseoul
from django.db.models import Max, Sum, Count



def dashboard(request):


    # seoul = Opexseoul.objects.all()
    # yangcheon_datas = Opexseoul.objects.values('restaurant').annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:5]

    # for re in seoul:
        # print(re.borough)

        # if re.borough == "yangcheon":

            # yangcheon = re.borough

            # print("t",yangcheon)



    yangcheon_datas = Opexseoul.objects.filter(borough='yangcheon').values('restaurant').annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:5]

    yongsan_datas = Opexseoul.objects.filter(borough='yongsan').values('restaurant').annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:5]

    yeongdeungpo_datas = Opexseoul.objects.filter(borough='yeongdeungpo').values('restaurant').annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:5]
    
    dobong_datas = Opexseoul.objects.filter(borough='dobong').values('restaurant').annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:5]


    gwangjin_datas = Opexseoul.objects.filter(borough='gwangjin').values('restaurant').annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:5]

    



    # print(yongsan_datas)

    # print(len(yangcheon_datas))
    # print(len(yongsan_datas))

    test = {
        "yangcheon_datas": yangcheon_datas,
        "yongsan_datas":yongsan_datas,
        "yeongdeungpo_datas":yeongdeungpo_datas,
        "dobong_datas":dobong_datas,
        "gwangjin_datas":gwangjin_datas,

    }
    
    # return render(request, 'dashboard/dashboard.html',{"yangcheon_datas":yangcheon_datas})
    return render(request, 'dashboard/dashboard.html',test)
    

    

    

            




    # yangcheon_datas = Opexseoul.objects.values('restaurant').annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:5]
        # elif re.borough == "yongsan":
        #     yongsan_datas = Opexseoul.objects.values('restaurant').annotate(name_count=Count('restaurant')).filter(name_count__gt=1).order_by('-name_count')[:5]

        

    return render(request, 'dashboard/dashboard.html')
        
        




    # return render(request, 'dashboard/dashboard.html',{"yangcheon_datas":yangcheon_datas})

    # seoul_datas = Opexseoul.objects.values()

    
    





    # return render(request, 'dashboard/dashboard.html',{"seoul_datas":seoul_datas})

    # recent_posts = Opexseoul.objects.order_by('-personnel')[:5]
    # print(len(seoul_datas))
    # print(seoul_datas)
    # rd = {}
    # print(rd['restaurant'])
    # for test_data in seoul_datas:
        # print(test_data)
        # print(test_data['restaurant'])
        # print(test_data['name_count'])
        # test_data = test_data
        # print(data)
        # rd['restaurant'] = 'name_count'
        # print(test_data['restaurant'])
        # print(test_data['name_count'])
        # data_name = data['restaurant']
        # data_num = data['name_count']
        # test_data = test_data
        # rd[test_data['restaurant']] = test_data['name_count']
        # rd[test_data['restaurant']] = test_data['name_count']
        # restaurant = test_data['restaurant']
        # name_count = test_data['name_count']
        # p_num = test_data['name_count']
        # print(p_num)
        # datas = {
            # "restaurant":restaurant,
            # "name_count":name_count
        # }
        # rd[test_data['restaurant']] = test_data['name_count']
        
        
    


    # r = test['restaurant']
    # for test in seoul_datas:
        # print(test)
        # print(test['restaurant'])
        # test = test['restaurant']
        # print(test)
        # print(list(test))
        # if test['restaurant'] not in rd:
            # rd[test['restaurant']]
        # print(rd)
            
            
            

        
        
        
    # print(seoul_datas)
    # rd = []
    # num = 0
    # i = 0

    # total = []

    # total2 = {}
    
    # for test in seoul_datas:

    #     i = test['personnel']
    #     r = test['restaurant']
    #     # print(test)
    #     # print(test['restaurant'])
    #     # cd = test['restaurant']
    #     # if test['restaurant'] not in rd:
    #     #     rd.append(r)
    #     #     # print(rd)
    #     # elif test['restaurant'] in rd:
    #     #     total.append({r:i})


    #     if test['restaurant'] not in rd:
    #         rd[r] = i 
    #         print(len(rd))
    #     elif test['restaurant'] in rd:
    #         rd[r] += i


    # print()
    
    # print(len(total))
    # print(total[0])

        
        
        
        # print(test['restaurant'])
        # print(test[3])
            # print(test)
        # if test['restaurant'] not in name:
            # name += test['restaurant']

        # for i in test:
            
        #     if i not in name:
        #         name += i


    # print(len(rd))
        # print(len(rd))
    # recent_posts = Opexseoul.objects.order_by('-personnel')[:5]
    
    

    # return render(request, 'dashboard/dashboard.html',{"rd":rd,"recent_posts":recent_posts})




        # result = 
        # print(result)
        
    # name = Opexseoul.objects.values('restaurant').distinct()

    # print(seoul_datas)

    # seoul_datas = Opexseoul.objects.all()
    





    # for cd in seoul_datas:
    #     # print(cd.price)
        
    #     # print(cd.restaurant)
    #     # cd.restaurant = set(cd.restaurant)

    #     # print(cd.restaurant)

    #     # result = set(cd.restaurant)
    #     # result = list(cd.restaurant)

    # # for cd in seoul_datas:


    # # name = Opexseoul.objects.distinct().values_list('restaurant')
    
    #     name = cd.restaurant
    #     # result = set(name)
    #     # result = sum(name)
    #     # result = str(name)
    #     # result = sum(result)
    #     result = list(name)
    #     result = ''.join(result)

    #     result = set(result)
        
        
    #     # result = list(result)
    #     print(result)
    

        

        
        # print(result)

    
    
    


    # return render(request, 'dashboard/dashboard.html', {"seoul_datas":seoul_datas})
    # return render(request, 'dashboard/dashboard.html')






