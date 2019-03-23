# _*_ encoding:utf-8 _*_
from django.shortcuts import render
from django.views.generic import View
from .models import CourseOrg, CityDict

from pure_pagination import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
class OrgView(View):
    # 课程机构列表功能
    def get(self, request):
        # 机构
        all_orgs = CourseOrg.objects.all()
        # 城市
        all_citys = CityDict.objects.all()
        print(all_orgs)
        print(all_citys)
        # 对课程机构进行分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_orgs,2, request=request)

        orgs = p.page(page)

        # return render_to_response('index.html', {
        #     'people': people,
        # }
        return render(request, "org-list.html", {
            "all_orgs":orgs,
            "all_citys":all_citys,
            "org_nums": len(all_orgs)
        })