from enum import Enum


class RelationTypeEnum(str, Enum):
    CONTINUES = "Continues"
    HASMETADATA = "HasMetadata"
    ISDERIVEDFROM = "IsDerivedFrom"
    ISIDENTICALTO = "IsIdenticalTo"
    ISNEWVERSIONOF = "IsNewVersionOf"
    ISPARTOF = "IsPartOf"
    ISSUPPLEMENTEDBY = "IsSupplementedBy"
    ISSUPPLEMENTTO = "IsSupplementTo"
    ISVARIANTFORMOF = "IsVariantFormOf"

    def __str__(self) -> str:
        return str(self.value)
