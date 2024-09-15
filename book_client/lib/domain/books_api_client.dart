import 'package:book_client/domain/book.dart';
import 'package:dio/dio.dart';
import 'package:book_client/app_urls.dart';

class BooksApiClient {
  final Dio dioClient;

  BooksApiClient({required this.dioClient});

  Future<List<Book>> loadBooks() async {
    final response = await dioClient.get(
      AppUrls.allBooks,
    );
    final body = response.data as Map<String, dynamic>;
    final books = (body['books'] as List<dynamic>)
        .map(
          (task) => Book.fromJson(task as Map<String, dynamic>),
        )
        .toList();
    return books;
  }
}
