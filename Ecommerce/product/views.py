from .models import CoffeeMachine, CoffeePod
from .serializer import ListCoffeeMachinesSerializer, ListCoffeePodSerializer
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .utils import *
# Create your views here.


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_all_coffee_machines(request):
    """
    :param request:
    :return: list of coffee machines as json object
    """
    coffee_machines = CoffeeMachine.objects.all()
    coffee_machines_serializer = ListCoffeeMachinesSerializer(coffee_machines, many=True)
    return Response({"coffee_machines": coffee_machines_serializer.data}, 200)


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_all_coffee_machines_by_type(request):
    """
    :param request: get product_type in request
    :return: list of coffee machines filtered by product_type as json object
    """
    if "product_type" not in request.data:
        return Response({"error": "please send product type"})
    product_type = request.data.get("product_type")
    if product_type not in coffee_machines_product_type.keys():
        return Response({"error": "invalid product type"})
    product_type_enum = coffee_machines_product_type[product_type]
    coffee_machines = CoffeeMachine.objects.filter(product_type=str(product_type_enum))
    coffee_machines_serializer = ListCoffeeMachinesSerializer(coffee_machines, many=True)
    return Response({"coffee_machines": coffee_machines_serializer.data}, 200)


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_all_coffee_machines_by_water_line(request):
    """
    :param request: get water_line_compatible in request
    :return: list of coffee machines filtered by water_line_compatible as json object
    """
    if "water_line_compatible" not in request.data:
        return Response({"error": "please send water line compatible"})
    water_line_compatible = request.data.get("water_line_compatible")
    coffee_machines = CoffeeMachine.objects.filter(water_line_compatible=water_line_compatible)
    coffee_machines_serializer = ListCoffeeMachinesSerializer(coffee_machines, many=True)
    return Response({"coffee_machines": coffee_machines_serializer.data}, 200)


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_all_coffee_pods(request):
    """
    :param request:
    :return: list of coffee pods as json object
    """
    coffee_pods = CoffeePod.objects.all()
    coffee_pods_serializer = ListCoffeePodSerializer(coffee_pods, many=True)
    return Response({"coffee_pods": coffee_pods_serializer.data}, 200)


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_all_coffee_pods_by_type(request):
    """
    :param request: get product_type in request
    :return: list of coffee pods filtered by product_type as json object
    """
    if "product_type" not in request.data:
        return Response({"error": "please send product type"})
    product_type = request.data.get("product_type")
    if product_type not in coffee_pods_product_type.keys():
        return Response({"error": "invalid product type"})
    product_type_enum = coffee_pods_product_type[product_type]
    coffee_pods = CoffeePod.objects.filter(product_type=str(product_type_enum))
    coffee_pods_serializer = ListCoffeePodSerializer(coffee_pods, many=True)
    return Response({"coffee_pods": coffee_pods_serializer.data}, 200)


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_all_coffee_pods_by_flavor(request):
    """
    :param request: get coffee_flavor in request
    :return: list of coffee pods filtered by coffee_flavor as json object
    """
    if "coffee_flavor" not in request.data:
        return Response({"error": "please send coffee flavor"})
    coffee_flavor = request.data.get("coffee_flavor")
    if coffee_flavor not in coffee_pods_flavor.keys():
        return Response({"error": "invalid coffee flavor"})
    coffee_flavor_enum = coffee_pods_flavor[coffee_flavor]
    coffee_pods = CoffeePod.objects.filter(coffee_flavor=str(coffee_flavor_enum))
    coffee_pods_serializer = ListCoffeePodSerializer(coffee_pods, many=True)
    return Response({"coffee_pods": coffee_pods_serializer.data}, 200)


@api_view(["GET"])
@permission_classes((AllowAny,))
def get_all_coffee_pods_by_pack_size(request):
    """
    :param request: get pack_size in request
    :return: list of coffee pods filtered by pack_size as json object
    """
    if "pack_size" not in request.data:
        return Response({"error": "please send pack size"})
    pack_size = request.data.get("pack_size")
    coffee_pods = CoffeePod.objects.filter(pack_size=str(pack_size))
    coffee_pods_serializer = ListCoffeePodSerializer(coffee_pods, many=True)
    return Response({"coffee_pods": coffee_pods_serializer.data}, 200)
