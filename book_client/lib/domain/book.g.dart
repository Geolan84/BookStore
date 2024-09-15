// GENERATED CODE - DO NOT MODIFY BY HAND

part of 'book.dart';

// **************************************************************************
// JsonSerializableGenerator
// **************************************************************************

Book _$BookFromJson(Map<String, dynamic> json) => Book(
      id: json['id'] as String,
      name: json['name'] as String,
      description: json['description'] as String,
      isbn: json['isbn'] as String,
      publisherId: (json['publisher_id'] as num).toInt(),
      photoUrl: json['photo'] as String?,
    );

Map<String, dynamic> _$BookToJson(Book instance) => <String, dynamic>{
      'id': instance.id,
      'name': instance.name,
      'description': instance.description,
      'photo': instance.photoUrl,
      'isbn': instance.isbn,
      'publisher_id': instance.publisherId,
    };
