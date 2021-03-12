from django.shortcuts import render

from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Rassilka
# Create your views here.
from .models import Rassilka, Groups, Topics, Answers, Users
import json
import datetime

#редактирование данных
#@renderer_classes((JSONRenderer))
@csrf_exempt
def index(request):
    if request.method == 'POST':
        results = request.POST
        print(results)
        import logging
        logging.debug(results)

        if "spec" in results:
            ff = Groups.objects.filter()
            for i in ff:
                i.peer_id_new = f"{i.peer_id}"
                i.save()
        if "date_start" in results:
            date_new = results["date_start"]
            id_ras = results["id"]
            ras = Rassilka.objects.get(id=id_ras)
            d = datetime.datetime.strptime(f"{date_new}", "%Y-%m-%dT%H:%M:%S")
            ras.date_start = d
            ras.save()

        elif "delete" in results:
            id_ras = results["id"]
            p = Rassilka.objects.get(id=id_ras)
            p.delete()

        elif "club_id" in results:
            #print(results["status"])
            #results = json.loads(results)
            if results["status"] == "1":
                #print(111)
                t = Groups.objects.filter(id_group=int(results["club_id"]))
                #print(t)
                t[0].bol = False
                t[0].stat = 1
                t[0].save()
            elif results["status"] == "2":
                t = Groups.objects.filter(id_group=int(results["club_id"]))
                f = 0
                peer_id = t[0].peer_id_new
                peer_id_spis = peer_id.split(", ")
                if peer_id_spis[0] == "0":
                    t[0].peer_id_new = f"{results['peer_id']}"
                    t[0].bol_peer_id = True
                    t[0].save()
                    f = 1
                elif peer_id_spis[0] != "0":
                    if results['peer_id'] not in peer_id_spis:
                        t.peer_id_new = f"{peer_id}, {results['peer_id']}"
                        t.save()
                        f = 1
                    #peer_id_news = peer_id.split(',')
                return JsonResponse({'status': '1', 'peer_id': f}, status=200)

        elif "create" in results:
            #print(dict(results["create"]))
            '''import pdb
            pdb.set_trace()'''
            #dd = dict(results)
            #print(results["create"])
            #dd = json.loads(results["create"])
            #print(dd)
            #print(results["create"].getlist)
            #resu = json.loads(results["create"])
            #print(resu)
            #print(i)
            #i = json.loads(i)
            t = Topics.objects.filter(soc=results["them"])
            if "peer_id" in results:
                bol_peer_id = True
                peer_id = results["peer_id"]
            else:
                bol_peer_id = False
                peer_id = 0
            params = {
                'name': results["name"],
                'token': results["token"],
                'id_group': results["id_group"],
                'peer_id': peer_id,
                'them_id': t[0].id,
                'link': f'https://vk.com/club{results["id_group"]}',
                'bol': True,
                'bol_peer_id': bol_peer_id,
                'stat': 1,
            }
            device = Groups.objects.create(**params)
            '''for i in results["create"]:
                #print(i)
                #i = json.loads(i)
                t = Topics.objects.filter(soc=i["them"])
                if i["peer_id"] == 0:
                    bol_peer_id = False
                else:
                    bol_peer_id = True
                params = {
                    'name': i["name"],
                    'token': i["token"],
                    'id_group': i["id_group"],
                    'peer_id': i["peer_id"],
                    'them_id': t[0].id,
                    'link': f'https://vk.com/club{i["id_group"]}',
                    'bol': True,
                    'bol_peer_id': bol_peer_id,
                    'stat': 1,
                }
                device = Groups.objects.create(**params)'''

        elif "get" in results:
            vse = Groups.objects.filter()
            tokens = []
            for i in vse:
                t = Topics.objects.filter(id=i.them_id)
                tokens.append({"id": i.id_group, "name": i.name, "token": i.token, "them": t[0].soc})
            return JsonResponse({'status': '1', "list": tokens}, status=200)

        elif "answer" in results:
            params = {
                'question_id': results["number"],
                'answer': results["answer"],
                'user_id': results["user_id_mongo"]
            }
            Answers.objects.create(**params)
        elif "create_users" in results:
            params = {
                'name': results["name"],
                'link': results["link"],
                'rating': results["rating"]
            }
            Users.objects.create(**params)

    return JsonResponse({'status': '1'}, status=200)

#https://djbook.ru/ch07s02.html

