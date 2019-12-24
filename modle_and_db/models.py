from django.contrib.postgres.fields import JSONField
from django.db import models

from modle_and_db.util import contact_default

'''
快速上手
'''


# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


'''
字段类型
'''


# https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/
class Field_Options(models.Model):
    # null Field.null
    # 如果设置为 True， 当该字段为空时，Django 会将数据库中该字段设置为 NULL，默认为 False
    # 避免在基于 字符串 的字段（例如 CharField 和 TextField）上使用 null

    # 那意味着对于“无数据”有两个可能的值：NULL 和空字符串。
    # 在大多数情况下，对于“无数据”声明两个值是赘余的，Django 的惯例是使用空字符串而不是 NULL

    # 一个例外是当 CharField 同时具有 unique=True 和 blank=True 时。
    # 在这种情况下，需要设置 null=True，以便在使用空白值保存多个对象时避免唯一的约束违规。

    # 对于基于字符串的字段和基于非字符串的字段，blank=True如果您希望在表单中允许使用空值，
    # 则还需要进行设置，因为该 null参数仅影响数据库存储（请参阅参考资料blank）
    field_1 = models.DateField(null=True)

    # blank
    # Field.blank
    # 如果设置为 True ，该字段允许为空。默认为 False 。
    # 请注意，这与有所不同null。null与数据库完全相关，而blank与验证相关。
    # 如果字段包含blank=True，则表单验证将允许输入一个空值。如果字段包含blank=False，则将需要该字段。
    field_2 = models.DateField(blank=True)

    # db_column
    # 用于此字段的数据库列的名称。如果未指定，Django将使用该字段的名称。
    field_3 = models.CharField(db_column='field_33', max_length=32)

    # db_index
    # Field.db_index
    # 如果为True，将为此字段创建数据库索引
    field_4 = models.CharField(db_index=True, max_length=32, default='')

    # db_tablespace
    # Field.db_tablespace
    # 如果此字段已建立索引，则用于该字段的索引的数据库表空间的名称。
    # 默认值是项目的 DEFAULT_INDEX_TABLESPACE设置（如果已设置），或者 db_tablespace是模型的设置（如果有）。
    # 如果后端不支持索引的表空间，则忽略此选项。

    # default
    # Field.default
    # 该变量的值。
    # 可以是一个值或者是一个可调用的对象，如果是个可调用对象，每次实例化模型时都会调用该对象。

    # 默认不能是可变对象（模型实例，list，set等），
    # 作为该对象的相同实例的引用将被用作在所有新的模型实例的默认值。
    # 而是将所需的默认值包装在可调用中。例如，如果要指定一个默认dict的 JSONField，使用函数：

    contact_info = JSONField("ContactInfo", default=contact_default)


# choices
# 本身由恰好两个项目（例如）的可迭代数组成 的序列，用作此字段的选择。
# 如果给出选择，则它们由模型验证强制执行，并且默认表单小部件将是具有这些选择的选择框，而不是标准文本字段。[(A, B), (A, B) ...]

# 每个元组中的第一个元素是要在模型上设置的实际值，第二个元素是人类可读的名称。例如：
class Student(models.Model):
    FRESHMAN = 'FR'
    SOPHOMORE = 'SO'
    JUNIOR = 'JR'
    SENIOR = 'SR'
    GRADUATE = 'GR'
    YEAR_IN_SCHOOL_CHOICES = [
        (FRESHMAN, 'Freshman'),
        (SOPHOMORE, 'Sophomore'),
        (JUNIOR, 'Junior'),
        (SENIOR, 'Senior'),
        (GRADUATE, 'Graduate'),
    ]
    year_in_school = models.CharField(
        max_length=2,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FRESHMAN,
    )

    def is_upperclass(self):
        return self.year_in_school in {self.JUNIOR, self.SENIOR}
