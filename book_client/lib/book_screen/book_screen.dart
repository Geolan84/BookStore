import 'package:book_client/domain/book.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';

class BookScreen extends StatelessWidget {
  final Book book;

  const BookScreen({required this.book, super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(),
      body: SingleChildScrollView(
        child: Column(
          children: [
            if (book.photoUrl != null)
              CachedNetworkImage(imageUrl: book.photoUrl!),
            Text(book.name),
            Text(book.description),
            Text(book.isbn),
          ],
        ),
      ),
    );
  }
}
