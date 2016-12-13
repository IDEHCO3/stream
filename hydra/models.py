from django.contrib.gis.gdal import SpatialReference, OGRGeometry
from django.contrib.gis.geos.prepared import PreparedGeometry
from django.db import models
from django.contrib.gis.geos import GEOSGeometry, Point, LineString, Polygon
from context_api.models import Class
# Create your models here.

class SupportedProperty(models.Model):
    property = models.CharField(max_length=100, blank=False, null=False)
    required = models.BooleanField(null=False)
    readable = models.BooleanField(null=False)
    writeable = models.BooleanField(null=False)
    hydra_class = models.ForeignKey(Class, blank=False, null=False, related_name='supported_properties')

class SupportedOperation(models.Model):
    identifier = models.CharField(max_length=1000, blank=True, null=True)
    type = models.CharField(max_length=100, blank=True, null=False)
    title = models.CharField(max_length=100, blank=False, null=False)
    method = models.CharField(max_length=100, blank=False, null=False)
    expects = models.ForeignKey(Class, null=True, related_name='operations_expects')
    returns = models.ForeignKey(Class, null=True, related_name='operations_returns')
    possible_status = models.CharField(max_length=100, blank=True, null=True)
    hydra_class = models.ForeignKey(Class, blank=False, null=False, related_name='supported_operations')


class Type_Called():
    def __init__(self, a_name, params, answer):
        self.name = a_name
        self.parameters = params
        self.return_type = answer

class FeatureModel(models.Model):

    def __init__(self, a_hyperlink):
        self.hyperlink = a_hyperlink
        self.dic = {}

    def centroid(self):
       return self.geom.centroid

    def ring(self):
        return self.geom.ring

    def crs(self):
        return self.geom.crs

    def wkt(self):
        return self.geom.wkt

    def srs(self):
        return self.geom.srs

    def hexewkb(self):
        return self.geom.hexewkb

    def equals_exact(self, other_GEOSGeometry, tolerance=0):
        return self.geom.equals_exact(other_GEOSGeometry, tolerance)

    def set_srid(self, a_srid):
        return self.geom.set_srid(a_srid)

    def hex(self):
        return self.geom.hex

    def has_cs(self):
        return self.geom.has_cs

    def area(self):
        return self.geom.area

    def extend(self):
        return self.geom.extend

    def wkb(self):
        return self.geom.wkb

    def geojson(self):
        return self.geom.geojson

    def relate(self, other_GEOSGeometry, pattern):
        return self.geom.relate(other_GEOSGeometry, pattern)

    def set_coords(self, coords):
        return self.geom.set_coords(coords)

    def simple(self):
        return self.geom.simple

    def geom_type(self):
        return self.geom.geom_type

    def set_y(self, y):
        return self.geom.set_y(y)

    def normalize(self):
        return self.geom.normalize

    def sym_difference(self, other_GEOSGeometry):
        return self.geom.sym_difference(other_GEOSGeometry)

    def valid_reason(self):
        return self.geom.valid_reason

    def geom_typeid(self):
        return self.geom.geom_typeid

    def valid(self):
        return self.geom.valid

    def ogr(self):
        return self.geom.ogr

    def coords(self):
        return self.geom.coords

    def num_coords(self):
        return self.geom.num_coords

    def get_srid(self):
        return self.geom.get_srid

    def distance(self, other_GEOSGeometry):
        return self.geom.distance(other_GEOSGeometry)

    def json(self):
        return self.geom.json

    def pop(self):
        return self.geom.pop

    def ewkb(self):
        return self.geom.ewkb

    def x(self):
        return self.geom.x

    def simplify(self, tolerance=0.0, preserve_topology=False):
        return self.geom.simplify(tolerance=0.0, preserve_topology=False)

    def set_z(self):
        return self.geom.set_z

    def buffer(self, width, quadsegs=8):
        return self.geom.buffer(width, quadsegs)

    def relate_pattern(self, other_GEOSGeometry, pattern):
        return self.geom.relate_pattern(other_GEOSGeometry, pattern)

    def z(self):
        return self.geom.z

    def num_geom(self):
        return self.geom.num_geom

    def coord_seq(self):
        return self.geom.coord_seq

    def dims(self):
        return self.geom.dims

    def get_y(self):
        return self.geom.get_y

    def tuple(self):
        return self.geom.tuple

    def y(self):
        return self.geom.y

    def convex_hull(self):
        return self.geom.convex_hull

    def get_x(self):
        return self.geom.get_x

    def index(self):
        return self.geom.index

    def boundary(self):
        return self.geom.boundary

    def kml(self):
        return self.geom.kml

    def touches(self, other_GEOSGeometry):
        return self.geom.touches(other_GEOSGeometry)

    def empty(self):
        return self.geom.empty

    def srid(self):
        return self.geom.srid

    def get_z(self):
        return self.geom.get_z

    def extent(self):
        return self.geom.extent

    def union(self, other_GEOSGeometry):
        return self.geom.union(other_GEOSGeometry)

    def intersects(self, other_GEOSGeometry):
        return self.geom.intersect(other_GEOSGeometry)

    def contains(self, other_GEOSGeometry):
        return self.geom.contains(other_GEOSGeometry)

    def hasz(self):
        return self.geom.hasz

    def crosses(self, other_GEOSGeometry):
        return self.geom.crosses(other_GEOSGeometry)

    def count(self):
        return self.geom.count

    def num_points(self):
        return self.geom.num_points

    def within(self, other_GEOSGeometry):
        return self.geom.within(other_GEOSGeometry)

    def intersection(self, other_GEOSGeometry):
        return self.geom.intersection(other_GEOSGeometry)

    def overlaps(self, other_GEOSGeometry):
        return self.geom.overlaps(other_GEOSGeometry)

    def equals(self, other_GeosGeometry ):
        return self.geom.equals( other_GeosGeometry)

    def point_on_surface(self):
        return self.geom.point_on_surface

    def difference(self, other_GEOSGeometry):
        return self.geom.difference(other_GEOSGeometry)

    def transform(self,srid, clone=True ):
        return self.geom.transform(srid, clone=True)

    def set_x(self, x):
        return self.geom.set_x(x)

    def get_coords(self):
        return self.geom.get_coords

    def envelope(self):
        return self.geom.envelope

    def prepared(self):
        return self.geom.prepared

    def ewkt(self):
        return self.geom.ewkt

    def length(self):
        return self.geom.length

    def disjoint(self, other_GEOSGeometry):
        return self.geom.disjoint(other_GEOSGeometry)

    def geometry_with_parameters_type(self):
        #self.dic = [   '', '', 'intersects', 'json', 'kml', 'length', 'normalize', 'num_coords', 'num_geom', 'num_points', 'ogr', 'overlaps', 'point_on_surface', 'pop', 'prepared', 'ptr', 'ptr_type', 'relate', 'relate_pattern', 'remove', 'reverse', 'ring', 'set_coords', 'set_srid', 'set_x', 'set_y', 'set_z', 'simple', 'simplify', 'sort', 'srid', 'srs', 'sym_difference', 'touches', 'transform', 'tuple', 'union', 'valid', 'valid_reason', 'within', 'wkb', 'wkt', 'x', 'y', 'z']

        if len(self.dic) == 0:
            self.dic['area'] = Type_Called('area', None, float)
            self.dic['boundary'] = Type_Called('boundary', None, float)
            self.dic['buffer'] = Type_Called('buffer', [float], GEOSGeometry)
            self.dic['centroid'] = Type_Called('centroid', None, Point)
            self.dic['contains'] = Type_Called('contains', [GEOSGeometry], bool)
            self.dic['convex_hull'] = Type_Called('convex_hull', None, Polygon)
            self.dic['coord_seq'] = Type_Called('coord_seq', None, tuple)
            self.dic['coords'] = Type_Called('coords', None, tuple)
            self.dic['count'] = Type_Called('count', None, int)
            self.dic['crosses'] = Type_Called('crosses', [GEOSGeometry], bool)
            self.dic['crs'] = Type_Called('crs', None, SpatialReference)
            self.dic['difference'] = Type_Called('difference', [GEOSGeometry], GEOSGeometry)
            self.dic['dims'] = Type_Called('dims', None, int)
            self.dic['disjoint'] = Type_Called('disjoint',[GEOSGeometry], bool)
            self.dic['distance'] = Type_Called('distance',[GEOSGeometry], float)
            self.dic['empty'] = Type_Called('empty',None, bool)
            self.dic['envelope'] = Type_Called('envelope',None, GEOSGeometry)
            self.dic['equals'] = Type_Called('equals',[GEOSGeometry], bool)
            self.dic['equals_exact'] = Type_Called('equals_exact',[GEOSGeometry, float], bool)
            self.dic['ewkb'] = Type_Called('ewkb',None, str)
            self.dic['ewkt'] = Type_Called('ewkt',None, str)
            self.dic['extend'] = Type_Called('extend',None, tuple)
            self.dic['extent'] = Type_Called('extent',None, tuple)
            self.dic['geojson'] = Type_Called('geojson',None, str)
            self.dic['geom_type'] = Type_Called('geom_type',None, str)
            self.dic['geom_typeid'] = Type_Called('geom_typeid',None, int)
            self.dic['get_coords'] = Type_Called('get_coords', None, tuple)
            self.dic['get_srid'] = Type_Called('get_srid', None, str)
            self.dic['get_x'] = Type_Called('get_x', None, str)
            self.dic['get_y'] = Type_Called('get_y', None, str)
            self.dic['get_z'] = Type_Called('get_z', None, str)
            self.dic['has_cs'] = Type_Called('has_cs',None, bool)
            self.dic['hasz'] = Type_Called('hasz',None, bool)
            self.dic['hex'] = Type_Called('hex',None, str)
            self.dic['hexewkb'] = Type_Called('hexewkb',None, str)
            self.dic['index'] = Type_Called('index',None, int)
            self.dic['intersection'] = Type_Called('intersection',[GEOSGeometry], GEOSGeometry)
            self.dic['intersects'] = Type_Called('intersects',[GEOSGeometry], bool)
            self.dic['interpolate'] = Type_Called('interpolate',[float], Point)
            self.dic['json'] = Type_Called('json',None, str)
            self.dic['kml'] = Type_Called('kml',None, str)
            self.dic['length'] = Type_Called('length',None, float)
            self.dic['normalize'] = Type_Called('normalize',[float], Point)
            self.dic['num_coords'] = Type_Called('num_coords',None, int)
            self.dic['num_geom'] = Type_Called('num_geom',None, int)
            self.dic['num_points'] = Type_Called('num_points',None, int)
            self.dic['ogr'] = Type_Called('ogr',None,  OGRGeometry)
            self.dic['overlaps'] = Type_Called('overlaps',[GEOSGeometry],  bool)
            self.dic['point_on_surface'] = Type_Called('point_on_surface',None,  Point)
            self.dic['pop'] = Type_Called('pop',None,  tuple)
            self.dic['prepared'] = Type_Called('prepared',None,  PreparedGeometry)
            self.dic['relate'] = Type_Called('relate',[GEOSGeometry],  str)
            self.dic['relate_pattern'] = Type_Called('relate_pattern',[GEOSGeometry, str],  str)
            self.dic['ring'] = Type_Called('ring',None,  bool)
            self.dic['set_coords'] = Type_Called('set_coords',[tuple],  None)
            self.dic['set_srid'] = Type_Called('set_srid',[str],  None)
            self.dic['set_x'] = Type_Called('set_x',[float],  None)
            self.dic['set_y'] = Type_Called('set_y',[float],  None)
            self.dic['set_z'] = Type_Called('set_z',[float],  None)
            self.dic['simple'] = Type_Called('simple',None,  bool)
            self.dic['simplify'] = Type_Called('simplify', [float, bool],  GEOSGeometry)
            self.dic['srid'] = Type_Called('srid', None,  int)
            self.dic['srs'] = Type_Called('srs', None,  SpatialReference)
            self.dic['sym_difference'] = Type_Called('sym_difference', [GEOSGeometry],  GEOSGeometry)
            self.dic['touches'] = Type_Called('touches', [GEOSGeometry],  bool)
            self.dic['transform'] = Type_Called('transform', [int, bool],  GEOSGeometry)
            self.dic['tuple'] = Type_Called('tuple', None,  tuple)
            self.dic['union'] = Type_Called('union', [GEOSGeometry],  GEOSGeometry)
            self.dic['valid'] = Type_Called('valid', [GEOSGeometry],  bool)
            self.dic['valid_reason'] = Type_Called('valid_reason', [GEOSGeometry],  str)
            self.dic['within'] = Type_Called('within', [GEOSGeometry],  bool)
            self.dic['wkb'] = Type_Called('wkb', None,  str)
            self.dic['wkt'] = Type_Called('wkt', None,  str)
            self.dic['x'] = Type_Called('x', None,  float)
            self.dic['y'] = Type_Called('y', None,  float)
            self.dic['z'] = Type_Called('z', None,  float)
        return self.dic















