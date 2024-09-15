import 'package:flutter/foundation.dart';
import 'package:json_annotation/json_annotation.dart';

part 'book.g.dart';

@immutable
@JsonSerializable()
class Book {
  final String id;

  final String name;

  final String description;

  @JsonKey(name: 'photo')
  final String? photoUrl;

  final String isbn;

  @JsonKey(name: 'publisher_id')
  final int publisherId;

  const Book({
    required this.id,
    required this.name,
    required this.description,
    required this.isbn,
    required this.publisherId,
    this.photoUrl,
  });

  factory Book.fromJson(Map<String, dynamic> json) => _$BookFromJson(json);

  Map<String, dynamic> toJson() => _$BookToJson(this);
}
