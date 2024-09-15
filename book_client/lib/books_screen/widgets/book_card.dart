import 'package:book_client/book_screen/book_screen.dart';
import 'package:book_client/domain/book.dart';
import 'package:cached_network_image/cached_network_image.dart';
import 'package:flutter/material.dart';

class BookCard extends StatelessWidget {
  final Book book;

  const BookCard({required this.book, super.key});

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: () {
        final detail = MaterialPageRoute(
          builder: (_) => BookScreen(book: book),
        );
        Navigator.push(context, detail);
      },
      child: Card(
        color: Colors.white,
        shape: RoundedRectangleBorder(
          borderRadius: BorderRadius.circular(10),
          side: const BorderSide(
            color: Colors.white,
          ),
        ),
        child: ClipRRect(
          borderRadius: BorderRadius.circular(10),
          child: Column(
            children: [
              book.photoUrl == null
                  ? const Icon(Icons.abc_outlined)
                  : CachedNetworkImage(
                      imageUrl: book.photoUrl!,
                      fit: BoxFit.cover,
                      placeholder: (context, url) =>
                          const CircularProgressIndicator.adaptive(),
                      errorWidget: (context, url, error) =>
                          const Text('без фото'),
                    ),
              Text(book.name),
            ],
          ),
        ),
      ),
    );
  }
}
